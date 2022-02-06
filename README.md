# restaurants-reservation

Suppose that you have a restaurant and you want to create an API for your customer to make a reservation.  

***Assumption***    
 - Your restaurant is open 24 hours.
 - Your restaurant has a total of 12 tables.
 - Every customer is allowed to make a reservation on one table for only 1 hour    
 **examples:** when Jim makes a reservation for table 6 at 12:00 then the table 6 will be available at 13:00.

## API Description

### 1. `GET` Get the reservation by name
Use `get` method to retrieve the details of the reservation by name of booker.

### 2. `GET` Get the all the reservation in one table.
Use `get` method to retrieve all the reservation in that table.

### 3. `POST` Make a reservation.

Use `post` method to make a reservation.

**Conditions:**
- Suppose that on table number 5 has a reservation at 10:00 AM. You can't make a reservation on that time and that table.

### 4. `Delete` Cancel the reservation
Use `delete` method to cancel the specific reservation by name and table number.

### 5. `Put` Update the reservation
Use `put` method to update the specific reservation.

**Conditions:**
- Suppose that on you have a reservation on table number 6 at 12:00 PM and you want to change a time to 15:00 PM. Unfortunately, table number 6 at 15:00 PM already reserved so the new reservation will not allowed. 
