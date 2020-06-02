# IoT-Remote-Lab

This is the Git Repository associated with the TUM IoT Remote Lab.

The folder structure is composed in the following way:
- Deliverable 1.1
	- Contains json schemas with their according payload
	- validation.py is used for validating json files against their schemas & assuring that references across schemas work to a sufficient grade.
- Delibverable 1.2
	- Contains the files that are related to the W3C WoT Thing Descriptions ([TD description](https://www.w3.org/TR/wot-thing-description/))
	- files with the prefix p_ are partial TD files, therefore validation in the TD playground will not be successful
	- files that I am unsure about because of possible misinterpretation of the exercise description:
		- p_links.json
		- robot1C.json
		- controller.json
		- startSystem.json, stopSystem.json, action1.json