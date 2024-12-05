var builder = WebApplication.CreateBuilder(args);

builder.WebHost.ConfigureKestrel(options =>
{
    options.ListenAnyIP(8000);
    options.ListenAnyIP(8443, listenOptions =>
    {
        listenOptions.UseHttps();
    });
});

builder.Services.AddOpenApi();

builder.Services.AddControllers();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

// app.UseHttpsRedirection(); # use incase of wanting to use https only

app.MapControllers();

app.Run();