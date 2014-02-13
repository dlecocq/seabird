---
layout: post
title:  "Custom Branding Iron"
date:   2014-01-10 12:00:00
categories: shop tools 3d
---

Following [an article](http://www.thefrankes.com/wp/?s=branding+iron) on how to
model a custom branding iron, I decided to take a stab at it. Here are some
notes on the process. My mission was to create a brand that was my signature.

Inkscape
--------
In order to get my signature in, I took a few tries with a sharpie and scanned
the best of these. Once scanned, Inkscape can `Trace Bitmap` which generates
a path the represents the signature. It's pretty noisy, so I simplified the path
a couple of times to smooth it and then deleted all the stray speckles and
control points. The remaining control points needed a little tuning in places to
get rid of some sharp points.

Repeat the same process to create a new path that will serve as the backing
plate for the signature. Export the SVG for the signature in one file and the
filled-in backing in another.

Blender
-------
Import the backing plate and the signature into Blender. Extrude the signature
by 0.625mm (for a total thickness of 1.25mm) and the backing plate by 1.5mm
(for a total thickness of 3mm, the minimum wall thickness for Shapeways). Offset
the backing plate to align it with the signature. __Remember to align it to the
appropriate face so that the text will be in the right orientation when used as
a branding iron.__

Convert each of these into meshes and `join` them. Export it as a collada file.

SketchUp
--------
The only reason to introduce SketchUp into the mix is so that we can scale the
signature to the exact dimensions. __Do not scale the thickness, but only the
height and width.__ While you're here, add a 1/4"-thick rod to the back so that
it can be attached to a handle.

Shapeways
---------
Finally, you're ready to use the model exported from SketchUp to upload it to
Shapeways (or another service) and order a print.
