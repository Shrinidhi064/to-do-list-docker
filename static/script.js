function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
}

// Live search (optional enhancement)
document.getElementById('search').addEventListener('keyup', function() {
  let filter = this.value.toLowerCase();
  let tasks = document.querySelectorAll('#task-list li');
  tasks.forEach(task => {
    let text = task.textContent.toLowerCase();
    task.style.display = text.includes(filter) ? '' : 'none';
  });
});