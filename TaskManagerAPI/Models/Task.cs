namespace TaskManagerAPI.Models
{
    public class Task
    {
        public int Id { get; set; }
        public required string Title { get; set; }
        public required string Description { get; set; }
        public bool Completed { get; set; } = false;
    }
}
