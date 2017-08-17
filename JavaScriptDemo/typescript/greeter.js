/**
 * 1. test type : string
 */
//function greeter(person : string) {
//	return "Hello, "+person;
//}
//var user = "Jane User";
//var user = [1, 2, 3];
function greeter(person) {
    return "Hello, " + person.firstName + " " + person.lastName;
}
//var user = {firstName: "Jane", lastName:"User"};
/**
 * 3. test type : class
 */
var Student = (function () {
    function Student(firstName, middlename, lastName) {
        this.firstName = firstName;
        this.middlename = middlename;
        this.lastName = lastName;
        this.fullname = firstName + " " + middlename + " " + lastName;
    }
    return Student;
}());
var user = new Student("Jane", "M.", "Malue");
document.body.innerHTML = greeter(user);
