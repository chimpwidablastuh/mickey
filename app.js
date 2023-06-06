const robot = require("robotjs");


setInterval(moveMouse, 10000);

function moveMouse(){
  // generate random position within the screen for the mouse
  let randomX = Math.floor(Math.random() * 1000);
  let randomY = Math.floor(Math.random() * 1000);
  // move the mouse to the random position
  robot.moveMouseSmooth(randomX, randomY);

}