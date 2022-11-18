import tkinter

class theme:
    def __init__(self):
        self.pri_font = "Space Grotesk"

        self.pri_bg = "#282c3c"
        self.sec_bg = "#282434"

        self.pri_button = "#f44c64"
        self.sec_button = "#fc7764"

        self.pri_table = "#4e486e"

class functions:
    def place(self, object, root, rel_x, rel_y, rel_height, rel_width):
        object.place(
            root,
            relx = rel_x,
            rely = rel_y,
            relheight = rel_height,
            relwidth = rel_width
        )

    def clear(self, root):
        for widget in root.winfo_children():
            widget.destroy()

class boiler:
    def __init__(self):
        self.theme = theme()

    def credit(self):
        credit = tkinter.Label(
            text = "An open source software, initialized by Alaqmar Gandhi, Haashir Firfire and Samridh Dey",
            font = (self.theme.pri_font, 8),
            bg = self.theme.pri_bg,
            fg = "white",
            padx = 5,
            pady = 10
        )

        credit.place(
            anchor = tkinter.SE,
            relx = 1,
            rely = 1
        )

    def top_bar(self, text, font_size, rel_height):
        top_bar = tkinter.Label(
            text = text,
            font = (self.theme.pri_font, font_size),
            bg = self.theme.sec_bg,
            fg = "white"
        )

        top_bar.place(
            relheight = rel_height,
            relwidth = 1
        )

        return top_bar

    def pri_button(self, root, text, font_size, command, anchor, rel_x, rel_y, rel_height, rel_width):
        button = tkinter.Button(
            root,
            text = text,
            font = (self.theme.pri_font, font_size),
            bg = self.theme.pri_button,
            fg = "white",
            activebackground = self.theme.sec_button,
            activeforeground = "white",
            relief = "flat",
            bd = 0,
            command = command
        )

        button.place(
            anchor = anchor,
            relx = rel_x,
            rely = rel_y,
            relheight = rel_height,
            relwidth = rel_width
        )

    def sec_button(self, root, text, font_size, command, anchor, rel_x, rel_y, rel_height, rel_width):
        button = tkinter.Button(
            root,
            text = text,
            font = (self.theme.pri_font, font_size),
            bg = self.theme.sec_button,
            fg = "white",
            activebackground = self.theme.pri_button,
            activeforeground = "white",
            relief = "flat",
            bd = 0,
            command = command
        )

        button.place(
            anchor = anchor,
            relx = rel_x,
            rely = rel_y,
            relheight = rel_height,
            relwidth = rel_width
        )

    def pri_input(self, root, input_value):
        input = tkinter.Entry(
            root,
            relief = "solid",
            bg = theme().sec_bg,
            fg = "white",
            font = (theme().pri_font, 20),
            justify = "center"
        )

        input.insert(
            0, 
            input_value
        )

        return input

class home:
    def __init__(self, root):
        functions().clear(root)
        boiler().credit()

        boiler().top_bar(
            "Resturant Management System",
            40,
            0.1
        )

        boiler().pri_button(
            root,
            "Login",
            35,
            self.login,
            tkinter.CENTER,
            0.5,
            0.5,
            0.1,
            0.2
        )

        boiler().pri_button(
            root,
            "Close",
            35,
            self.close,
            tkinter.CENTER,
            0.5,
            0.61,
            0.1,
            0.2
        )


    def login(self):
        main(root)

    def close(self):
        root.destroy()

dict_item = dict()
list_counter = -1
counter = 0

class overlay:
    def table_popup(self, table_button:tkinter.Button):
        self.table_button = table_button

        self.popup_frame = tkinter.Frame(
            bg = theme().pri_bg,
            borderwidth = 2,
            relief = "ridge"
        )

        self.popup_frame.place(
            relx = 0.5,
            rely = 0.5,
            anchor = tkinter.CENTER,
            relheight = 0.7,
            relwidth = 0.3
        )

        table_name = table_button["text"]
        self.name_input = boiler().pri_input(
            self.popup_frame,
            table_name
        )

        self.name_input.place(
            relheight = 0.05,
            relwidth = 0.8,
            anchor = tkinter.CENTER,
            relx = 0.5,
            rely = 0.05
        )

        self.items_frame = tkinter.Frame(
            self.popup_frame,
            relief = "solid",
            bg = theme().sec_bg,
            borderwidth = 1
        )

        self.items_frame.place(
            relheight = 0.65,
            relwidth = 0.8,
            anchor = tkinter.N,
            relx = 0.5,
            rely = 0.1
        )

        global list_counter

        if table_name in dict_item:
            for item in dict_item[table_name]:
                item_name = item
                list_counter += 1

                self.items_frame.columnconfigure(
                    0,
                    weight = 1
                )

                label = tkinter.Label(
                    self.items_frame,
                    text = item_name,
                    bg = theme().pri_bg,
                    fg = "white",
                    font = (
                        theme().pri_font, 
                        20
                    )
                )

                label.grid(
                    row = list_counter
                )

        boiler().pri_button(
            self.popup_frame,
            "Add Item",
            20,
            self.add_item,
            tkinter.CENTER,
            0.5, 
            0.8,
            0.05, 
            0.8
        )

        boiler().pri_button(
            self.popup_frame,
            "Save",
            20,
            self.save_button,
            tkinter.CENTER,
            0.5, 
            0.86,
            0.05, 
            0.8
        )

        boiler().pri_button(
            self.popup_frame,
            "Delete",
            20,
            self.close_button,
            tkinter.CENTER,
            0.5, 
            0.95,
            0.05, 
            0.8
        )

    def close_button(self):
        global counter

        counter -= 1

        if self.table_button["text"] in dict_item:
            del dict_item[
                self.table_button["text"]
            ]
        
        self.table_button.destroy()
        self.popup_frame.destroy()

    def save_button(self):
        table_name = self.name_input.get()
        item_list = list()

        for button in self.items_frame.winfo_children():
            item_list.append(
                button["text"]
            )
            
        dict_item[table_name] = item_list

        self.table_button["text"] = table_name
        self.popup_frame.destroy()

    def add_item(self):
        self.add_frame = tkinter.Frame(
            bg = theme().pri_bg,
            borderwidth = 2,
            relief = "ridge"
        )
        
        self.add_frame.place(
            relwidth = 0.2,
            relheight = 0.15,
            anchor = tkinter.CENTER,
            relx = 0.5,
            rely = 0.5
        )

        self.name = tkinter.Entry(
            self.add_frame,
            bg = theme().sec_bg,
            fg = "white",
            text = (
                theme().pri_font, 
                30
            ),
            justify = "center",
            relief = "solid"
        )

        self.name.place(
            relheight = 0.3,
            relwidth = 0.9,
            anchor = tkinter.CENTER,
            relx = 0.5,
            rely = 0.25
        )

        self.name.delete(
            0, 
            tkinter.END
        )

        self.name.insert(
            0, 
            "Item Name"
        )

        boiler().pri_button(
            self.add_frame,
            "Submit",
            20,
            self.submit,
            tkinter.CENTER,
            0.5,
            0.7,
            0.4,
            0.9
        )

    def submit(self):
        global list_counter

        item_name = self.name.get()
        list_counter += 1

        self.add_frame.destroy()

        self.items_frame.columnconfigure(
            0,
            weight = 1
        )

        label = tkinter.Label(
            self.items_frame,
            text = item_name,
            bg = theme().pri_bg,
            fg = "white",
            font = (
                theme().pri_font,
                20
            )
        )

        label.grid(
            row = list_counter
        )

class tables:
    def create_table(self, parent:tkinter.Frame):
        global counter

        if counter < 30:
            text = "Table", counter + 1
            column = counter
            row = 0

            table_button = tkinter.Button(
                parent,
                text = text,
                font = (theme().pri_font, 15),
                bg = theme().pri_button,
                fg = "white",
                activebackground = theme().pri_button,
                activeforeground = "white",
                relief = "flat",
                bd = 0,
                command = lambda: self.open_table(table_button),
                height = 5,
                width = 20
            )

            counter += 1
            
            while column >= 6:
                column -= 6
                row += 1

            table_button.grid(
                row = row,
                column = column,
                pady = 15,
                padx = 15
            )
        
    def open_table(self, table_button):
        overlay().table_popup(table_button)

class main:
    def __init__(self, root):
        self.root = root

        functions().clear(root)
        boiler().credit()

        top_bar = boiler().top_bar(
            "",
            40,
            0.05
        )

        boiler().pri_button(
            top_bar,
            "Logout",
            20,
            self.logout,
            tkinter.E,
            1,
            0.5,
            1,
            0.1
        )

        boiler().pri_button(
            root,
            "Add Table",
            20,
            self.add_table,
            tkinter.S,
            0.5,
            0.95,
            0.05,
            0.8
        )

        self.frame = tkinter.Frame(
            root,
            bg = theme().sec_bg
        )

        self.frame.place(
            anchor = tkinter.CENTER,
            relheight = 0.73,
            relwidth = 0.8,
            relx = 0.5,
            rely = 0.475
        )

    def logout(self):
        home(root)

    def add_table(self):
        tables().create_table(self.frame)


class app:
    def __init__(self, root):
        self.theme = theme()

        root.attributes(
            "-fullscreen", 
            True
        )
        root.configure(
            bg = self.theme.pri_bg
        )

        home(root)

root = tkinter.Tk()
app(root)
root.mainloop()
