# shopping-wishlist

This is a project from my class CS361 - Software Engineering I.
The program is a CLI a shopping software that keeps track of products wanting to buy, including their prices. 
The app uses the microservice architecture where the main program contacts other microservices using ZeroMQ.

The main program contains the features:
- Add a Product: Given the user is on the main screen, when they use the “add product” command and enter the required information, then the product is saved to the list and a confirmation message is displayed.
- View the Product List: Given a product list is stored locally, when the user uses the view product list command, then all products should be printed in a clear format.
- Delete a Product: Given a product is stored in the system, when the user uses the “delete” command and specifies the product, then it is removed from the list and a confirmation message is displayed.

The 3 microservices:
- Microservice B: Summary Generator
  - Given a valid list of products is stored in the system, when the user uses the Summary Generator microservice, then they will see the total number of products and the total price.
  - Given a valid list of products is stored in the system, when the user uses the Summary Generator microservice, then they will see the total number of products and the total price.

- Microservice C: Price Updater
  - Given a product is already stored in the wishlist, when the user chooses the product and enters a new price, then the microservice validates the data and sends permission for the main program to update its list.
  - Given a valid product is chosen, when the user provides a new price, then the price is added to the product’s price history, stored separately in the microservice database.
 
- Microservice D: List Exporter
  - Given a list of products is stored in the system, when the user uses the export feature, then the microservice will write it to a file in JSON format.
  - Given a valid wishlist is stored in the system, when the list is successfully exported to a JSON file, then a full file path is displayed.
 
The main program also calls an additional microservice A - Currency Converter, which is written by my teammate Michael Iu.
