window.onload = function () {
    var presentRadios = document.querySelectorAll('input[type="radio"][value="present"]');
    var absentRadios = document.querySelectorAll('input[type="radio"][value="absent"]');
    var presentCountDisplay = document.getElementById('presentNumber');
    var attendance = {};
    var presentCount = 0;

    // Initialize attendance as 'absent' for each student
    presentRadios.forEach(function (radio) {
        var studentId = radio.name.split('_')[1];
        attendance[studentId] = "absent";
    });

    // Event listener for 'present' radio buttons
    presentRadios.forEach(function (radio) {
        var studentId = radio.name.split('_')[1];
        radio.addEventListener('change', function () {
            if (this.checked && attendance[studentId] === "absent") {
                presentCount++;
                attendance[studentId] = "present";
            }
            presentCountDisplay.value = presentCount >= 0 ? presentCount : 0;
        });
    });

    // Event listener for 'absent' radio buttons
    absentRadios.forEach(function (radio) {
        var studentId = radio.name.split('_')[1];
        radio.addEventListener('change', function () {
            if (this.checked && attendance[studentId] === "present") {
                presentCount--;
                attendance[studentId] = "absent";
            }
            presentCountDisplay.value = presentCount >= 0 ? presentCount : 0;
        });
    });
};

// Function to show the alert box when attendance is submitted
function submitrecord() {
    document.getElementById('alertMessage').textContent = "Attendance Submitted Successfully";
    document.getElementById('alertBox').style.display = 'block';
}

// Function to show or hide the student list based on department selection
function showDepartments() {
    var selectElement = document.getElementById("department-select");
    var studentList = document.getElementById("student-list");

    if (selectElement.value !== "all") {
        studentList.style.display = "block";
    } else {
        studentList.style.display = "none";
    }
}

// Function to check if an image URL is valid by loading it
function isValidImage(url, callback) {
    var img = new Image();
    img.src = url;
    img.onload = function () { callback(true); }; // Image exists
    img.onerror = function () { callback(false); }; // Image does not exist
}

// Function to display student details in the popup modal
function showStudentDetails(name, rollNumber, photoUrl) {
    document.getElementById('studentName').textContent = name;
    document.getElementById('studentRoll').textContent = rollNumber;

    // Check if the photo URL is valid
    isValidImage(photoUrl, function (isValid) {
        if (isValid) {
            document.getElementById('studentPhoto').src = photoUrl;
        } else {
            // Fallback to a default photo if the provided URL is invalid
            document.getElementById('studentPhoto').src = '/static/images/students.webp';
        }
    });

    document.getElementById('studentModal').style.display = 'block';
}

// Function to close the popup modal
function closeModal() {
    document.getElementById('studentModal').style.display = 'none';
}
