from tkinter import *
from tkinter import ttk
import mysql.connector as con

def getval():
    try:
        # Connect to the database
        c = con.connect(host='localhost', user='root', passwd='Gayatri@123', database='train_details')
        cursor = c.cursor()

        # Retrieve values from entry fields
        from_value = str(fromvalue.get())
        to_value = str(tovalue.get())

        # Execute SQL query
        query = '''
    SELECT 
        T.train_id AS "Train ID",
        T.train_name AS "Train Name",
        S1.name AS "Boarding Station",
        S2.name AS "Destination Station"
    FROM 
        trains T
    JOIN 
        stations S1 ON T.source_station_id = S1.Station_id
    JOIN 
        stations S2 ON T.destination_station_id = S2.Station_id
    WHERE 
        S1.name = %s AND S2.name = %s;
    '''

        cursor.execute(query, (from_value, to_value))
        rows = cursor.fetchall()

        # Create a new window to display the results
        root1 = Toplevel()
        root1.geometry("600x400")
        root1.configure(bg="#FFFFFF")

        # Create a treeview to display data in tabular form with scrollbar
        tree = ttk.Treeview(root1, columns=("Train ID", "Train Name", "Boarding Station ID", "Destination Station ID"), show="headings")
        tree.heading("#1", text="Train ID")
        tree.heading("#2", text="Train Name")
        tree.heading("#3", text="Boarding Station ID")
        tree.heading("#4", text="Destination Station ID")

        # Set column widths
        tree.column("#1", width=100)
        tree.column("#2", width=150)
        tree.column("#3", width=150)
        tree.column("#4", width=150)

        # Insert data into the treeview
        for row in rows:
            tree.insert("", "end", values=row)

        tree.pack(fill="both", expand=True)

    except con.Error as e:
        # Handle database connection errors
        print("Error connecting to MySQL database:", e)

# Main window
root = Tk()
root.title("TRAIN RESERVATION SYSTEM")
root.geometry("1000x1000")
root.minsize(400, 400)

# Create a canvas
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()

# Load the background image
image_path = "C:/Users/Atuln singh/Downloads/Trains (1).png"
background_image = PhotoImage(file=image_path)
canvas.create_image(0, 0, anchor=NW, image=background_image)

# Title label
Label(root, fg="black", bg="white", text="𝐇𝐄𝐋𝐋𝐎 𝐓𝐇𝐈𝐒 𝐈𝐒 𝐁𝐎𝐎𝐊𝐈𝐍𝐆 𝐓𝐈𝐂𝐊𝐄𝐓 𝐂𝐎𝐔𝐍𝐓𝐄𝐑", font="comicsans 20 bold", anchor="center", relief="sunken").place(x=405, y=20)

# Entry fields
fromvalue = StringVar()
tovalue = StringVar()
Entry(root, textvariable=fromvalue, bg="#F2CCC3", fg="black", borderwidth=5, relief=SUNKEN, font="arial 15 bold", justify=CENTER).place(x=600, y=130, width=150, height=40)
Entry(root, textvariable=tovalue, bg="#F2CCC3", fg="black", borderwidth=5, relief=SUNKEN, font="arial 15 bold", justify=CENTER).place(x=600, y=200, width=150, height=40)

# Labels for entry fields
Label(root, text="FROM \nWHICH DESTINATION", fg="black", bg="#B98EA7", font="Roboto 12 bold bold", borderwidth=3, relief=RAISED).place(x=390, y=130)
Label(root, text="TO \nWHICH DESTINATION", bg="#B98EA7", font="Hellvattica 12 bold", borderwidth=3, relief=RAISED).place(x=390, y=200)

# Button to trigger data retrieval
Button(root, bg="#7F055F", fg="#E5A4CB", borderwidth=3, relief=RAISED, justify=CENTER, text="CLICK ME! \n TO CHECK INFORMATION", font="arial 15 bold", command=getval).place(x=420, y=400)

root.mainloop()
