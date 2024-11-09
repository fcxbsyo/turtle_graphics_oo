# Polygon Art Generator
This program generates different types of polygonal art using turtle graphics.
User can choose 9 different art styles.

## Features
- Generates different polygon shapes.
- Random size, color, and orientation of the polygons each time.
- Some choices generate nested polygons.

## Requirements
- Python 3.8 and above
- Turtle graphics

## How to Run the Program
1. Clone or download the polygon_art.py file to your local machine.
2. Open a terminal or command prompt and navigate to the directory.
3. Run the program by the following command: "python polygon_art.py"
4. The program will prompt you with the following message: 
"Which art do you want to generate? Enter a number between 1-9 inclusive: "
5. Enter a number between 1-9 to select art to generate.

## Available Art Choices
- Choice 1: Draws a triangle.
- Choice 2: Draws a square.
- Choice 3: Draws a pentagon.
- Choice 4: Draws a polygon with random sides.
- Choice 5: Draws 3 triangles nested inside each other.
- Choice 6: Draws 3 quadrilaterals nested inside each other.
- Choice 7: Draws 3 pentagons nested inside each other.
- Choice 8: Draws 3 polygons with random sides nested inside each other.
- Choice 9: Combines random polygons and nested shapes in a single drawing.

## Known Issues
- Randomized Art: The art will look different each time you run the program due to randomization 
in size, color, position, and orientation.
- Performance Issues: For very large sizes or a large number of nested polygons, the program may slow down.
- No Exit: The turtle window will remain open until manually closed. 
The program does not automatically exit when the art is finished.

## Bugs
- Potential Bug: There may be performance issues if too many polygons are drawn at once.