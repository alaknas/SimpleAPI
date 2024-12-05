using Microsoft.AspNetCore.Mvc;
using Task = TaskManagerAPI.Models.Task;

namespace TaskManagerAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class TaskController : ControllerBase
    {
        private static List<Task> tasks = new List<Task>();

        [HttpPost]
        public IActionResult CreateTask([FromBody] Task task)
        {
            task.Id = tasks.Count + 1;
            tasks.Add(task);
            return CreatedAtAction(nameof(GetTaskById), new { id = task.Id }, task);
        }

        [HttpGet]
        public IActionResult GetAllTasks()
        {
            return Ok(tasks);
        }

        [HttpGet("summary")]
        public IActionResult GetSummary()
        {
            var taskCount = tasks.Count;
            var completedCount = tasks.Count(t => t.Completed);
            var summary = (TotalTasks: taskCount, CompletedTasks: completedCount, PendingTasks: taskCount - completedCount);
            return Ok(summary);
        }

        [HttpGet("pending")]
        public IActionResult GetPendingTasks()
        {
            var pendingTasks = tasks
                .Where(t => !t.Completed)
                .Select(t => new { t.Id, t.Title, t.Description })
                .ToList();
            return Ok(pendingTasks);
        }

        [HttpGet("{id}")]
        public IActionResult GetTaskById(int id)
        {
            var task = tasks.FirstOrDefault(t => t.Id == id);
            if (task == null) return NotFound();
            return Ok(task);
        }

        [HttpPut("{id}")]
        public IActionResult UpdateTask(int id, [FromBody] Task updatedTask)
        {
            var task = tasks.FirstOrDefault(t => t.Id == id);
            if (task == null) return NotFound();
            task.Title = updatedTask.Title;
            task.Description = updatedTask.Description;
            task.Completed = updatedTask.Completed;
            return NoContent();
        }

        [HttpDelete("{id}")]
        public IActionResult DeleteTask(int id)
        {
            var task = tasks.FirstOrDefault(t => t.Id == id);
            if (task == null) return NotFound();
            tasks.Remove(task);
            return NoContent();
        }
    }
}
