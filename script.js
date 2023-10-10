document.addEventListener('DOMContentLoaded', function () {
    const apiUrl = 'http://127.0.0.1:8000/todos/';  // Update with your FastAPI endpoint
    const form = document.getElementById('todo-form');
    const todoList = document.getElementById('todo-list');

    // Function to fetch and display todos
    function getTodos() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                todoList.innerHTML = ''; // Clear the list
                data.forEach(todo => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `${todo.title}: ${todo.description}`;
                    todoList.appendChild(listItem);
                });
            });
    }

    // Handle form submission
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const titleInput = document.getElementById('todo-title');
        const descriptionInput = document.getElementById('todo-description');

        const newTodo = {
            title: titleInput.value,
            description: descriptionInput.value
        };

        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newTodo)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            getTodos(); // Refresh the list
            form.reset(); // Clear the form
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    // Initial fetch of todos
    getTodos();
});
