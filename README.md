# Image Shuffler
Python 3 script which takes individual images of up to two different types, and shuffles them into a random grid.
Originally created for use in a JCU School of Psychology honors project, which involved measuring how quickly and accurately a subject could determine how many faces in a 5X4 grid of faces had "aggressive" - rather than "neutral" expressions.

## Requirements
Working as of Python 3.6.9

## Useage
With desired images in the appropriate folders - "type-a" and, optionally, "type-b" (see File Structure below), run the program and enter the desired number of matrices, type a images and type b images, and click "GO". Finalized matrices will appear in the "out" folder.
- number of matrices: This is the number of resulting matrices that are desired
- number of images of type a: This is the number of type_a images that will be selected to populate each matrix
- number of images of type b: This is the number of type_b images that will be selected. Leave this blank if you have only one type of image

## File Structure
```md
image-shuffler
|
+-- image_shuffler.py
|
+-- in
|  |
|  +-- type-a
|  |
|  +-- type-b
|
+-- out
```

## License
MIT License

Copyright (c) 2020 Josh Dickie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
