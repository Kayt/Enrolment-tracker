$(document).ready(function () {
    $("#new_enrolment").on("submit", function (event) {
        $(".loader").show();
        data = {};

        data["student"] = $("#all_students").val();
        data["course"] = $("#all_courses").val();
        data["year"] = $("#year").val();

        data_json = JSON.stringify(data);

        $.ajax({
            data:data_json,
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            url: "http://127.0.0.1:5000/enrolment"
        }).done(function (data) {
            if (data.error) {
                $(".loader").hide();

               
               

            } else {
                getData();
                $("#enrollment").html("");
                $(".loader").hide();
                $("#enroll_student").modal('hide');
            }
        });

        event.preventDefault();
    });
});

$(document).ready(function () {
    $("#new_course").on("submit", function (event) {
        $(".loader").show();
        data = {};

        data["name"] = $("#course_name").val();
        data["description"] = $("#course_desc").val();

        data_json = JSON.stringify(data);
        new_url = "http://127.0.0.1:5000/course/" + $("#course_name").val();

        $.ajax({
            data:data_json,
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            url: new_url
        }).done(function (data) {
            if (data.error) {
                $(".loader").hide();
            } else {
                getData();
                $(".loader").hide();
                $("#newCourse").modal('hide');
            }
        });

        event.preventDefault();
    });
});

$(document).ready(function () {
    $("#new_student").on("submit", function (event) {
        $(".loader").show();
        data = {};

        data["name"] = $("#student_name").val();
        data["surname"] = $("#student_surname").val();

        data_json = JSON.stringify(data);
        new_url = "http://127.0.0.1:5000/student/" + $("#student_name").val();

        $.ajax({
            data:data_json,
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            url: new_url
        }).done(function (data) {
            if (data.error) {
                $(".loader").hide();
            } else {
                getData();
                $(".loader").hide();
                $("#newStudent").modal('hide');
            }
        });

        event.preventDefault();
    });
});



function getData() {
    $("#courses").html("");
    $("#students").html("");
    $("#enrollment").html("");
    $("#all_courses").html("");
    $("#all_students").html("");


    getCourses();
    getEnrollment();
    getStudents();
   

}

function getCourses() {
    $(document).ready(function () {
        $.ajax({
            url: "http://127.0.0.1:5000/courses",
            type: "GET",
            dataType: "json", // added data type
            success: function (res) {
                response = res.courses;

                $.each(response, function (i, item) {
                    $("#courses").append('<tr> <td>' + item.name + '</td><td>' +
                        item.description + '</td>');
                    $("#all_courses").append('<option value="' + item.name + '">' +
                        item.name + ' </option>')
                });
            }
        });
    });
}

function createCSV() {
    $(document).ready(function () {
        $("#statusResult").modal('show');
        $.ajax({
            url: "http://127.0.0.1:5000/generate_csv",
            type: "GET",
            dataType: "json", // added data type
            success: function (res) {
                
                
                
            }
        });
    });
}

function getEnrollment() {
    $(document).ready(function () {
        $.ajax({
            url: "http://127.0.0.1:5000/enrolments",
            type: "GET",
            dataType: "json", // added data type
            success: function (res) {
                response = res.enrolments;

                $.each(response, function (i, item) {
                    $("#enrollment").append('<tr> <td>' + item.student +
                        '</td><td>' + item.course + '</td></td><td>' + item.year +
                        '</td>');

                });
            }
        });
    });
}

function getStudents() {
    $(document).ready(function () {
        $.ajax({
            url: "http://127.0.0.1:5000/students",
            type: "GET",
            dataType: "json", // added data type
            success: function (res) {
                response = res.students;

                $(function () {

                    $.each(response, function (i, item) {
                        $("#students").append('<tr> <td>' + item.name +
                            '</td><td>' + item.surname + '</td>');
                        var full_name = item.name + ' ' + item.surname;
                        $("#all_students").append('<option value="' +
                            full_name + '">' + full_name + ' </option>'
                        );
                    });


                });
            }
        });
    });
}