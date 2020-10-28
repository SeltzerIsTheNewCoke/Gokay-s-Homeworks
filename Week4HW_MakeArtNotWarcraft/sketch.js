var CircleX = 0;

function setup() {
  createCanvas(700, 500);
  background(229);
  for (var i = 0;
       i <100;
       i ++){
        fill(random(255),random(255),random(255));
        stroke(0,0,0);
        strokeWeight(4);
        triangle(random(200),random(200),random(200),random(200),random(500),random(500));
        fill(random(255),random(255),random(255));
        rectMode(CENTER);
        rect(random(1000),65,random(75));
        fill(random(255),random(255),random(255));
        ellipse(random(255),random(31),random(500),random(50));
        point(49,50);
        point(90,31);
}
}

function draw() {

}
