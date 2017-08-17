/**
 * 1. test type : string
 */
//function greeter(person : string) {
//	return "Hello, "+person;
//}
//var user = "Jane User";
//var user = [1, 2, 3];


/**
 * 2. test type : interface 
 * Person 接口
 */
interface Person {
	firstName : string;
	lastName  : string;
}
function greeter( person : Person ) {
	return "Hello, "+person.firstName + " " + person.lastName;
}
//var user = {firstName: "Jane", lastName:"User"};


/**
 * 3. test type : class
 */
class Student {
	fullname : string;
	constructor( public firstName, public middlename, public lastName ) {
		this.fullname = firstName + " " + middlename + " " + lastName;
	}
}
var user = new Student("Jane", "M.", "Malue");


document.body.innerHTML = greeter(user);

