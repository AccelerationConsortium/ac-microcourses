document.addEventListener("DOMContentLoaded", function() {
    // Define an async function to fetch and update student counts
    async function updateStudentCounts() {
        // Initially set the student count elements to show a loading message or spinner
        const studentCountElements = document.querySelectorAll('helloWorldStudentCount');
        studentCountElements.forEach(element => {
            element.innerHTML = 'Loading...'; // Or use an HTML spinner here
        });

        try {
            const apiUrl = 'https://jn36gg5cbhv7cagcojjiqitche0waqmc.lambda-url.us-east-2.on.aws/';
            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();

            // Assuming the API returns an object like { hello_world_student_count: 100, ... }
            // Update the student count and remove the loading message/spinner
            document.getElementById('helloWorldStudentCount').innerText = data.hello_world_student_count || 'N/A';
            // Repeat for other courses, matching their respective IDs
        } catch (error) {
            console.error('Failed to fetch student counts:', error);
            // Optionally handle errors, e.g., by setting a default text or removing the loading indicator
            studentCountElements.forEach(element => {
                element.innerHTML = 'N/A'; // Or any error message
            });
        }
    }

    // Call the function to update student counts
    updateStudentCounts();
});
