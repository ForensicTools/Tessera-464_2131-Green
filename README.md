Tessera
=======
Author: Kayla Green

Front-end wrapper for The Volatility Framework.

This tool acts as an interactive, easier-to-use wrapper around the already popular Volatility framework. Currently the tool is written in python and uses subprocess calls (ew, I know) due to the cumbersome nature of the Volatility libraries. 

Usage
------
Call/Run program using:<br />
<code>./tessera</code> <br />

After booting, Tessera will ask if you'd like to make a case. <br />
Creating a case means that all information entered will be stored in a file for easy record keeping. <br />
Choosing no skips the case building option. <br />>
Choosing yes brings you into the case building menu. Case takes a string for input. <br />
<p><code>	Enter case name: 		Case#067 - Mark Phillips<br />
</code> </p>
Tessera will then ask for a list of investigator names. Terminate the list by entering a "." <br />
<p><code>	Enter investigator names: <t> 	John Doe <br />
				 <t><t><t>	Mary Sue<br /> 
				<t><t><t>	.<br />	 
</code></p>
The next portion asked for is the location of the memory dump that is being analyzed; this location is verified by Tessera, so if Tessera can't find the image, it will ask for a new location.<br />
<code>	Enter full path to image: 	/home/john/forensics/mark.img</code><br />

Tessera then will hash the image using the SHA-1 algorithm. This hash will be displayed to you. If you chose to build a case, this information will be stored in a file at the end of the Tessera run. 

Tessera then takes the image and runs imageinfo on it to get a list of profiles. It automatically lists these and then asks you to choose a number. If no number is specified (you just hit enter), it will grab the first option. If you choose OTHER, it will prompt for a profile name. This must be a valid profile that Volatility knows about. <br />
<p><code>	Profile appears to be: <br />
	1. WIN7SP0x64  <br />
	2. WIN7SP1x64  <br />
	3. OTHER 	<br />
	Choose profile:		 	3 <br />
	Enter profile:			WIN2008R2SP0x64<br />
</code></p>
Tessera will then attempt to built the case with the information that you have given it. If the case was successfully built and Tessera runs into no problems, it will inform the user of its success. Otherwise it will (hopefully) exit gracefully.<br />
<<t>code>	Case successfully built.</code><br />

From here on out, Tessera will ask questions about what type of information you want to get from the image. List of supported plugins can be found in the plugins.txt file. By default, this is the same list of plugins in the standalone copy of the Volatility Framework. To call a plugin, simply type in its name.

Information gathered will be found in a directory located in the CWD where the image file sits in this format:<br />
<t><t> <code>/IMAGE_LOCATION/Tessera/case_file/output</code>

In addition, a hail mary option is available to drill through all available plugins. This is not a smart function and does not perform OS detection; use at your own risk. 
					 		

Future Additions
----------------
1. Create log of volatility commands utilized on backend (FINISHED)
2. Create base Tessera config file to store commonly chosen items (investigator names, etc.) 
3. Generate LaTeX-built Forensic Reports of Collected Information and Commands Issued
4. Rebuild in C++ for Speed and easier transport
