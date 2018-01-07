/**
 * Tutorial 0: Writing Programs with Javascript
 * This is largely a replication of code examples for a fast pick-up of Javascript language
 */

// If statement (examples from codeAcademy):

var stopLight = 'green';

if (stopLight === 'red') {
    console.log('Stop');
} else if (stopLight === 'yellow') {
    console.log('Slow down');
} else if (stopLight === 'green') {
    console.log('Go!');
} else {
    console.log('Caution, unknown!');
}


// Introducing Switch function
var train = 'full';
var badweather = false;
switch (train) {
    case 'full':
        console.log('Sold Out');
        break;
    case 'notsold':
        console.log('Not on Sale');
        break;
    case 'not full':
        console.log('Tickets Available');
        break;
    default:
        console.log('Invalid');
        break;
}

// Examples of Writing a function: the most important is to understand its workflow!
var orderCount = 0;

function takeOrder(topping, crustType) {
    console.log('Order: ' + crustType + ' crust topped with ' + topping);
    orderCount = orderCount + 1;
}

function getSubTotal(itemCount) {
    return itemCount * 7.5;
}

function getTax() {
    return getSubTotal(orderCount) * 0.06;
}

function getTotal() {
    return getSubTotal(orderCount) + getTax();
}


takeOrder('bacon', 'thin');
takeOrder('pepperoni', 'regular');
takeOrder('pesto', 'thin');

console.log(getSubTotal(orderCount));
console.log(getTotal());


// Arrays
var bucketList = ['Amazon', 'Facebook', 'Google'];
// js counts stuff from 0, 1, 2, 3...
var listItem = bucketList[0];
console.log(listItem);
// .length can check both number of variables and a string
console.log(bucketList.length);
console.log('bucketList'.length);
// Some manipulations, see what it can do
bucketList.push('Twitter', 'Microsoft');
console.log(bucketList);
bucketList.pop();
console.log(bucketList);
bucketList.shift();
console.log(bucketList);
bucketList.unshift('Amazon', 'Linkedin');
// try + instead of , btw two items, what happened?
console.log(bucketList);
var pos = bucketList.indexOf('Linkedin');
console.log(pos);
bucketList.splice(pos,2);
//what does the number following the pos mean?
console.log(bucketList);

// Introducing global scope and local scope * you may skip this if this sounds familiar to you in any other languages
function myApartment() {
	var myCoffeeMaker = 'Aeropress';
	
	var myCloset = 'Extra coats in the back';
	
	var myRefridgerator = 'Filled with veggies and dark chocolate.';
	var myDog = 'Nikko';
	
}

// What happen if you switch something out from the myApartment function?
var buildingAddress = '150 E 14th St, New York, NY';
var buildingLaundryCode = 4927;
var buildingPhone = '(481) 516-2342';


console.log("**Apartment Building Information**");
console.log("Laundry code: " + buildingLaundryCode + "\nPhone: " + buildingPhone + "\nMailing address: " + buildingAddress);

// For loop:
var vacationSpots = ['Paris', 'Osaka', 'Kyoto'];

for (var i = 0; i < vacationSpots.length; i++) {
  console.log('I would love to visit ' + vacationSpots[i]);
}

//backwards, but why start from -1?
for (var i = vacationSpots.length-1; i>=0; i--) {
  console.log('I would love to visit ' + vacationSpots[i]);
}
// if statement within the for loop, look carefully what it produced
var myPlaces = ['Beijing','Shanghai', 'Fukuoka'];
var friendPlaces = ['Seattle', 'Fukuoka', 'Beijing'];

for (var i = 0; i < myPlaces.length; i++) {
    console.log(myPlaces[i]);
  
  for (var j = 0; j < friendPlaces.length; j++) {
        console.log(friendPlaces[j]);
    
    if (myPlaces[i] === friendPlaces[j]) {
    			console.log('Match: ' + myPlaces[i]);
				}
    }
}
/** Results:
Beijing
Seattle
Fukuoka
Beijing
Match: Beijing
Shanghai
Seattle
Fukuoka
Beijing
Fukuoka
Seattle
Fukuoka
Match: Fukuoka
Beijing
**/
// While loop, pretty easy to understand: (example from codeAcademy)
var cards = ['Diamond', 'Spade', 'Heart', 'Club'];

var currentCard = 'Heart';

while (currentCard !== 'Spade') {
  console.log(currentCard);

  var randomNumber = Math.floor(Math.random() * 4);

  currentCard = cards[randomNumber];
}

console.log('Found a Spade!');
// Some mild treatment of jQuery
// jQuert command line:
<script src='https://code.jquery.com/jquery-3.1.0.min.js'></script>
// It should be put before:
<script src='js/main.js'></script> 
//which is the main html file using
// Select elements and do some interactive thing
function main() {
  $('.skillset').hide();
  $('.skillset').fadeIn(1000);
  
  $('.projects').hide();
  
  $('.projects-button').on('click', function() {
	//$(this).next().toggle();
  	//$(this).text('Projects Viewed');
	//$(this).next().toggle();
    	//$(this).next().slideToggle(400);
	});
}

$(document).ready(main);
