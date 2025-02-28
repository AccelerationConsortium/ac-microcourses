document.addEventListener("DOMContentLoaded", function() {
    // Define an async function to fetch and update student counts
    async function updateStudentCounts() {
        // Initially set the student count elements to show a loading message or spinner
        const studentCountElements = document.querySelectorAll('.helloWorldStudentCount');
        studentCountElements.forEach(element => {
            element.innerHTML = 'Loading...'; // Or use an HTML spinner here
        });

        const apiUrl = 'https://jn36gg5cbhv7cagcojjiqitche0waqmc.lambda-url.us-east-2.on.aws/';

        // Define the retry mechanism
        async function fetchWithRetry(url, retries = 3, backoff = 3000) {
            for (let i = 0; i < retries; i++) {
                try {
                    const response = await fetch(url);
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return await response.json();
                } catch (error) {
                    if (i < retries - 1) {
                        console.warn(`Attempt ${i + 1} failed. Retrying in ${backoff}ms...`);
                        await new Promise(resolve => setTimeout(resolve, backoff));
                        backoff *= 2; // Exponential backoff
                    } else {
                        throw error;
                    }
                }
            }
        }

        try {
            const data = await fetchWithRetry(apiUrl);

            // Assuming the API returns an object like { hello_world_student_count: 100, ... }
            // Update the student count and remove the loading message/spinner
            document.getElementById('helloWorldStudentCount').innerText = data.hello_world_student_count || 'N/A';
            document.getElementById('helloWorldCompletionCount').innerText = data.hello_world_completion_count || 'N/A';
            document.getElementById('dataScienceStudentCount').innerText = data.data_science_student_count || 'N/A';
            document.getElementById('dataScienceCompletionCount').innerText = data.data_science_completion_count || 'N/A';
            document.getElementById('roboticsStudentCount').innerText = data.robotics_student_count || 'N/A';
            document.getElementById('roboticsCompletionCount').innerText = data.robotics_completion_count || 'N/A';
            document.getElementById('softwareDevStudentCount').innerText = data.software_dev_student_count || 'N/A';
            document.getElementById('softwareDevCompletionCount').innerText = data.software_dev_completion_count || 'N/A';
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
