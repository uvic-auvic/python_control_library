# Python Control Library
Simple python library for controling motors on polaris.

## How To Use
Within the script you would like to use this library, type
<pre>
from control import controls
</pre>
At the top of the script. To use the library methods, initialize an instance of the class by typing.
<pre>
c = controls(1)
</pre>
Where 1 is the serial communications port that polaris uses to communicate with the motor controller.
</br>
</br>
Methods can now be called like the following:
<pre>
c.activate_motor(1, 50)
</pre>
Methods are explained in the Wiki
