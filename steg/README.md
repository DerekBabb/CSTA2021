# Lab 9 - CYBR 2980

## Steganography
[Introduction Video](https://use.vg/4xN4YE)  

Steganography is a method for concealing information within seemingly innocent media. The true craft comes from sending the information in a manner so that only the sender and the intended recipient realize its existence. Steganography may be as simple as altering the language of a message. It can also involve using a ""container", such as a jpg image, to carry a "cargo" of data, such as a text file. However the message is concealed, the art is in hiding the data in plain sight so as to hide its true intention. With steganography, seemingly unaltered images, video files, sound files, and even blank disc space can all inconspicuously carry extra data.

#### Example Techniques of Steganography
**Color -> Letter Conversion:**  
Colors:  Every color on a computer is represented as a mixture of red, green and blue colors.  Since everything is digital, at its rawest level, these colors are simply binary 0s and 1s.

Letters:  Similarly to colors, every letter on the keyboard or in a message has a binary representation based on the ASCII standard.  For example, the letter 'A' is the number 65 on the ASCII conversion chart.  One easy way to hide information in an image is to simply change an entire color to the number from a single letter.  For example, say you wanted to hide the message "Hello World" in an image.  We could find the ASCII value of each of those letters and change the Red value of every 13th pixel to match that data.  This method will leave visual artifacts of the modification.

**Least Significant Bit:** This method is much more difficult to detect but also more difficult to implement.  In the least significant bit (LSB) method, we change rightmost bit of each color to match our data.  For example in the pixel color  (Red = 178, Green = 216, Blue = 222) if we switch to the binary values we get: (10110010, 11011000, 11011110).  Since the letter 'H' is ASCII 72 is 01001000 in binary, we can begin hiding the data from this 'H' across the red, green and blue of many pixels in the rightmost bit by making this change: 10110010, 11011001, 11011110.  The next pixel would have the right three bits values be changed to **0, 1, 0** with the remaining values of H's ASCII in the next pixel's right most bits.  This process can be continued to hide an entire message.
![LSB ExampleImage](https://blog.switchfast.com/hs-fs/hubfs/Threats%20Hiding%20in%20Plain%20Sight%20Digital%20Steganography%20on%20the%20Rise.png?width=600&name=Threats%20Hiding%20in%20Plain%20Sight%20Digital%20Steganography%20on%20the%20Rise.png)

### Steganography App
Our challenge today is to build a steganography app that can take a message and encode it into an image. Alternatively we want to be able to read an image and decode the hidden message.

#### Helper Functions
**numberToBinary(num)**  
The point of this function is to take a number in base 10 and convert it to a binary string. We will make the return value be a full byte (8-bits) and as a result the largest value that we will be able to convert is the number 255.
This type of precondition is a state that we expect for all values coming in. We could verify the number is in the range 0-255 but that is the stated expectation for anyone using our function.

- Why are we using a string result?
- How can we calculate a binary value in an algorithm?
- How do we ensure that the result is 8-bits, even if the number doesn't need that many bits?

[Video Demonstration of Function](https://use.vg/9k1bEW)  


**binaryToNumber(binaryString)**
This function will take a binary string and return a base 10 number.
- Working from right to left, is the last digit a 1 or a 0?
- Thinking back to our binary lesson, how can I calculate the value of each number?
- How do we know that we are done?


**encode(img, message)**
This function will take an image and a message as parameters. We will then convert each letter in the message to binary. The binary values will be spread across the least significant bits (LSB) of the RGB values for the image.
- Since each letter takes 8 bits, how many pixels will we need per letter?
- Is there a maximum size to our message? How would we calculate that?
- How will we visit every pixel in an orderly way?
- When we are done with all the letters in a message, how do we stop the function?

When we have encoded the message in the image, we should save this new image to be loaded later.

[Video Demonstration - Part 1](https://use.vg/kEz3P5)  
[Video Demonstration - Part 2](https://use.vg/vDKePo)  


**decode(img)**
This function will take an image as parameter. This image has been encoded with a secret message using the technique that we have created in our encode function.
- Read the length of the encoded message.
- Convert the colors to binary for each pixel.
- Since it takes three pixels to get one letter, how do we build the letter binary?
- Convert the binary back into a number.
- Convert the number back to a letter.

**main()**
The main function should drive the rest of the application.
- Ask the user if they are encoding or decoding.
- Prompt for the image that will be opened.
- If encoding, prompt for a message to encode.
- If decoding, display the decoded message.

## End of class
In Repl.it, you will find the share link to your code. That is what gets submitted to Canvas.
