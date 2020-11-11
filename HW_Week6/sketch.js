var sizeSlider;
 
function setup() {
  createCanvas(850,850);
  
  sizeSlider = createSlider(1, 100, 50); //100 is max, 50 is defaut start)
  sizeSlider.position(50, 50);
}
 
function draw() 
{
  background(255);
  fill(50);
  textAlign(CENTER);
  textFont("Helvetica");
  textSize(sizeSlider.value()); 
  text("Text Size: " + sizeSlider.value(), width/2, height/2); 
}