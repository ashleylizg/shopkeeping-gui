# shopkeeping-gui
Observe and edit a small shop inventory in a SQLite database using tkinter.

## Initial Set-Up
Clone this repository and go into the main folder:

```git clone <this_repo>```

```cd shopkeeping-gui```

Establish a SQLite database with the column names (name, quantity, price) and respective data types:

```python setup.py```

## Usage
**Open the main window**:

```python window.py```

<br />

![Main GUI](https://github.com/ashleylizg/shopkeeping-gui/blob/main/images/mainscreen.PNG)

* **Add a new record**: 
  * Type in entry boxes for name, quantity, and price. 
  * Hit the 'Add Record to Database' button.

* **Show existing records**:
  * Hit the 'Show Records' button.
<br /> ![Show Records](https://github.com/ashleylizg/shopkeeping-gui/blob/main/images/show-records.PNG)
* **Calculate price of certain quantity of items in stock**:
  * Specify an item by its ID in the Select ID entry box. 
  * Choose quantity for price sum. 
  * Hit 'Calculate Price Sum' button. 
  * When finished, use the 'Clear Output' button.
<br /> ![Calculate Price](https://github.com/ashleylizg/shopkeeping-gui/blob/main/images/calculate-price.PNG)
* **Update a record**:
  * Specify an item by its ID in the Select ID entry box. 
  * Hit the 'Update Record' button. 
  * In the new window, adjust desired attributes for name, quantity, and price then hit the 'Save Record' button.
<br /> ![Update Record](https://github.com/ashleylizg/shopkeeping-gui/blob/main/images/edit-inventory.PNG)
* **Delete a record**:
  * Specify an item by its ID in the Select ID entry box. 
  * Hit the 'Delete Record' button.
