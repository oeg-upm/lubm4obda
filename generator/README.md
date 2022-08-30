## Build and run the data generator image locally

Clone this repository:

`git clone https://github.com/oeg-upm/lubm4obda.git`

Then get into this directory:

`cd lubm4obda/generator`

Build the image:

`docker build -t lubm4obda .`

Run the image:

`docker run -itv "$(pwd)":/output lubm4obda`
