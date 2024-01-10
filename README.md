Microsoft Flight Simulator X has a feature where you can ask for the real-life weather conditions in the location you were in. This made the playing experience much more realistic. Unfortunately, the feature stopped working, and the only options are for the user to customize or create their own weather or to user pre-made weather conditions. 
The scope of this project is to try and fix this issue for the user to be able to have a semi-real experience in weather conditions they are flying in.  

The weather interface was done in Python. It works by quering data from a weather API, using the JSON and request packages. Then, using list indexing, the data is sorted in order to fetch only some necessary data which will be used later on.
In order to make the project more user-friendly, the tkinter library was used in order to develop a GUI. This GUI has a search bar, in order for the user to enter the zip code of the location, and it has a search button. Once the button is clicked, given the zip code, the quering process begins.

The user can use this interface, in order to see all the info it needs weather related, and create their own personalized weather, but entering real-life data of said location. This creates semi-realistic weather conditions. 
