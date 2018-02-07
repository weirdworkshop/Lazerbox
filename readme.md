#Lazerbox readme

Lazerbox is a script for  Autodesk Fusion 360 that generates a sketch of a notched 'fingerjoint' box that is suitable for laser cutting.


Lazerbox builds on the [Boxmaker] (https://github.com/lukecyca/BoxMaker)  but does not generate the object and uses the notch style of [Makercase] (http://www.makercase.com/)

##Installation

To install Lazerbox into Fusion 360 follow the [instructions] 
(https://knowledge.autodesk.com/support/fusion-360/troubleshooting/caas/sfdcarticles/sfdcarticles/How-to-install-an-ADD-IN-and-Script-in-Fusion-360.html)

lazerbox is a script, so make sure to install into the correct location for a script

Once installed Lazerbox can be accessed from ADD-INS > Scripts and Add-Ins . It should appear in the My Scripts section


##Running

Enter the dimensions of the box that you require.  These are the outside dimensions
Enter the material thickness that you will be using.
Enter the width of the notches that you want to create.

The notch width  should be no smaller than the thickness of the material and no larger than 20% of the smallest of the three dimensions (Width,Height, Depth)

Optionally select an existing component to generate the sketch onto.

Hit ok and a sketch will be created.



