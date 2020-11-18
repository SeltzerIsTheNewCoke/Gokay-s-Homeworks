let cam;

function setup() {
  createCanvas(500, 500,WEBGL);
  cam = createCapture (VIDEO);
  cam.size(320, 240);
  cam.hide();
  noStroke();
  rectMode(CENTER);
}


function draw() {
  background(0);
  fill(0);
  texture(cam)
  rect(mouseX, height / 2, mouseY / 2 + 10, mouseY / 2 + 10);
  fill(0);
  texture(cam)
  let inverseX = width - mouseX;
  let inverseY = height - mouseY;
  rect(inverseX, height / 2, inverseY / 2 + 10, inverseY / 2 + 10);
}