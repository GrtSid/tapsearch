# tapsearch

Steps to use TapSearch :
1) Create a virtualenv using python 3.5.4
2) activate the virtualenv
3) Clone the repository and change directory using
    cd tapsearch
4) install the libraries using 
    pip install -r requirements.txt
5) run flask server
    export FLASK_APP=main.py
    flask run
    Open the local server url on the browser and now you can use the TapSearch API.
    
  Sample Inputs and Outputs:
  Two documents (paragraphs) separated by two new lines (\n\n)

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna ac placerat vestibulum lectus. Elit duis tristique sollicitudin nibh sit amet commodo. Senectus et netus et malesuada fames. Fermentum iaculis eu non diam phasellus vestibulum lorem sed. Dictumst quisque sagittis purus sit amet volutpat consequat mauris. Aliquam ut porttitor leo a diam sollicitudin tempor. Consectetur a erat nam at lectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque. 



Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat in egestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eu tincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id venenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id.

Sample search

Input - lorem

Results: Paragraph 1 and 2 are returned

Input - Maecenas

        Results: Paragraph 1
        
Vision for the project:
1) As it is an efficient way to search, this could be used to retrieve data from database.
2) We can use it as a KeyWord extractor. Many companies want a efficient way to search for keywords in there datasets. Like. Hotel companies want to search for keywords like "Good" in there reviews.
3) The access logs and other similar logs concerning the security of the systems can be analyzed.
