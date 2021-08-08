# MARK TRISTAN FABELLAR, THEODORE JOHN DAMIRAY, HARRY ESCASINAS
# CPE 2 - 2

# An offline jeepney fare guide mobile application


from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from routes import *


class RouteOne(FloatLayout):
    Builder.load_file('route1.kv')


class RevRouteOne(FloatLayout):
    Builder.load_file('revroute1.kv')


class RouteTwo(FloatLayout):
    Builder.load_file('route2.kv')


class RevRouteTwo(FloatLayout):
    Builder.load_file('revroute2.kv')


class RouteThree(FloatLayout):
    Builder.load_file('route3.kv')


class RevRouteThree(FloatLayout):
    Builder.load_file('revroute3.kv')


class MainWindow(Screen):

    Builder.load_file('main_window.kv')

    def category_(self, checkbox, active):
        if active:
            self.ids.status.text = "Student/ Elderly/ Disabled"
        else:
            self.ids.status.text = "Regular"


class SecondWindow(Screen):

    Builder.load_file('second_window.kv')

    # Route 1

    def route1(self):
        return_button = MDFlatButton(
            text='SUBMIT',
            on_release=self.close_dialog,
        )

        self.dialog = MDDialog(
            title="Starting Place",
            type="custom",
            content_cls=RouteOne(),
            size_hint=(0.9, 1),
            buttons=[
                return_button
            ],
        )

        self.dialog.open()

    def revroute1(self):
        return_button = MDFlatButton(
            text='SUBMIT',
            on_release=self.close_dialog,
        )

        self.dialog = MDDialog(
            title="Destination",
            type="custom",
            content_cls=RevRouteOne(),
            size_hint=(0.9, 1),
            buttons=[
                return_button
            ],
        )

        self.dialog.open()

    # Route1: Validate Inputs
    def validate1(self):
        starting_place1 = self.ids.starting_place1.text
        destination1 = self.ids.destination1.text
        passenger1 = self.ids.passenger1.text
        minimum_fare1 = self.ids.minimum_fare1.text

        if (starting_place1 == ''
                or destination1 == ''
                or starting_place1 not in starting_place_1
                or destination1 not in starting_place_1
                or not passenger1.isnumeric()
                or not minimum_fare1.isnumeric()
                or int(passenger1) < 1
                or int(minimum_fare1) < 1):
            self.invalid_input()

        else:
            self.output1()
            self.manager.current = "output"
            self.manager.transition.direction = "left"

    def refresh1(self):
        self.ids.starting_place1.text = ''
        self.ids.destination1.text = ''
        self.ids.passenger1.text = '1'
        self.ids.minimum_fare1.text = '9'

    # Route1: Output
    def output1(self):
        status = self.manager.main.status.text
        starting_place1 = self.ids.starting_place1.text
        destination1 = self.ids.destination1.text
        passenger1 = self.ids.passenger1.text
        minimum_fare1 = self.ids.minimum_fare1.text

        # Status and Discount
        if status == "Regular":
            self.manager.output.status.text = "Regular"
            self.manager.output.discount.text = "None"
        else:
            self.manager.output.status.text = "Discounted"
            self.manager.output.discount.text = "20%"

        # Transit
        self.manager.output.transit.text = starting_place1+" - "+destination1

        # Total

        # Getting the distance of starting place and destination in km
        distance1 = int(starting_place_1.index(starting_place1))
        distance2 = int(starting_place_1.index(destination1))

        # Subtracting the distance of the two to get the final distance
        total_distance1 = abs(distance1 - distance2)

        self.manager.output.distance.text = str(total_distance1) + " KM"

        # Number of passenger
        number_of_passenger = int(passenger1)

        # Minimum Fare
        minimum_fare = int(minimum_fare1)

        # When the total distance is less than 4 then the tentative cost = 9 (Minimum Fare)
        if total_distance1 <= 4:
            tentative_cost = minimum_fare * number_of_passenger
        # Else, the total distance is the result of the formula below.
        else:
            tentative_cost = (((total_distance1 - 4) * 1.50) + minimum_fare) * number_of_passenger

        # If status is student/ elderly/ disabled, discount is 20%
        if status == "Regular":
            fare_cost = tentative_cost
        else:
            discount_ = round((tentative_cost * 0.20), 2)
            fare_cost = tentative_cost - discount_

        self.manager.output.total.text = "₱ " + str('{:.2f}'.format(fare_cost))  # The fare cost

    # Route 2
    
    def route2(self):
        return_button = MDFlatButton(
            text='SUBMIT',
            on_release=self.close_dialog,
        )

        self.dialog = MDDialog(
            title="Starting Place",
            type="custom",
            content_cls=RouteTwo(),
            size_hint=(0.9, 1),
            buttons=[
                return_button
            ],
        )

        self.dialog.open()

    def revroute2(self):
        return_button = MDFlatButton(
            text='SUBMIT',
            on_release=self.close_dialog,
        )

        self.dialog = MDDialog(
            title="Destination",
            type="custom",
            content_cls=RevRouteTwo(),
            size_hint=(0.9, 1),
            buttons=[
                return_button
            ],
        )

        self.dialog.open()

    # Route2: Validate Inputs
    def validate2(self):
        starting_place2 = self.ids.starting_place2.text
        destination2 = self.ids.destination2.text
        passenger2 = self.ids.passenger2.text
        minimum_fare2 = self.ids.minimum_fare2.text

        if (starting_place2 == ''
                or destination2 == ''
                or starting_place2 not in starting_place_2
                or destination2 not in starting_place_2
                or not passenger2.isnumeric()
                or not minimum_fare2.isnumeric()
                or int(passenger2) < 1
                or int(minimum_fare2) < 1):
            self.invalid_input()

        else:
            self.output2()
            self.manager.current = "output"
            self.manager.transition.direction = "left"

    # Route2: Output
    def output2(self):
        status = self.manager.main.status.text
        starting_place2 = self.ids.starting_place2.text
        destination2 = self.ids.destination2.text
        passenger2 = self.ids.passenger2.text
        minimum_fare2 = self.ids.minimum_fare2.text

        # Status and Discount
        if status == "Regular":
            self.manager.output.status.text = "Regular"
            self.manager.output.discount.text = "None"
        else:
            self.manager.output.status.text = "Discounted"
            self.manager.output.discount.text = "20%"

        # Transit
        self.manager.output.transit.text = starting_place2+" - "+destination2

        # Total

        # Getting the distance of starting place and destination in km
        distance1 = int(starting_place_2.index(starting_place2))
        distance2 = int(starting_place_2.index(destination2))

        # Subtracting the distance of the two to get the final distance
        total_distance2 = abs(distance1 - distance2)

        self.manager.output.distance.text = str(total_distance2) + " KM"

        # Number of passenger
        number_of_passenger2 = int(passenger2)

        # Minimum Fare
        minimum_fare2 = int(minimum_fare2)

        # When the total distance is less than 4 then the tentative cost = 9 (Minimum Fare)
        if total_distance2 <= 4:
            tentative_cost = minimum_fare2 * number_of_passenger2
        # Else, the total distance is the result of the formula below.
        else:
            tentative_cost = (((total_distance2 - 4) * 1.50) + minimum_fare2) * number_of_passenger2

        # If status is student/ elderly/ disabled, discount is 20%
        if status == "Regular":
            fare_cost = tentative_cost
        else:
            discount_ = round((tentative_cost * 0.20), 2)
            fare_cost = tentative_cost - discount_

        self.manager.output.total.text = "₱ " + str('{:.2f}'.format(fare_cost))  # The fare cost

    def refresh2(self):
        self.ids.starting_place2.text = ''
        self.ids.destination2.text = ''
        self.ids.passenger2.text = '1'
        self.ids.minimum_fare2.text = '9'

    # Route 3
    
    def route3(self):
        return_button = MDFlatButton(
            text='SUBMIT',
            on_release=self.close_dialog,
        )

        self.dialog = MDDialog(
            title="Starting Place",
            type="custom",
            content_cls=RouteThree(),
            size_hint=(0.9, 0.9),
            buttons=[
                return_button
            ],
        )

        self.dialog.open()

    def revroute3(self):
        return_button = MDFlatButton(
            text='SUBMIT',
            on_release=self.close_dialog,
        )

        self.dialog = MDDialog(
            title="Destination",
            type="custom",
            content_cls=RevRouteThree(),
            size_hint=(0.9, 1),
            buttons=[
                return_button
            ],
        )

        self.dialog.open()

    # Route3: Validate Inputs
    def validate3(self):
        starting_place3 = self.ids.starting_place3.text
        destination3 = self.ids.destination3.text
        passenger3 = self.ids.passenger3.text
        minimum_fare3 = self.ids.minimum_fare3.text

        if (starting_place3 == ''
                or destination3 == ''
                or starting_place3 not in starting_place_3
                or destination3 not in starting_place_3
                or not passenger3.isnumeric()
                or not minimum_fare3.isnumeric()
                or int(passenger3) < 1
                or int(minimum_fare3) < 1):
            self.invalid_input()

        else:
            self.output3()
            self.manager.current = "output"
            self.manager.transition.direction = "left"

    # Route3: Output
    def output3(self):
        status = self.manager.main.status.text
        starting_place3 = self.ids.starting_place3.text
        destination3 = self.ids.destination3.text
        passenger3 = self.ids.passenger3.text
        minimum_fare3 = self.ids.minimum_fare3.text

        # Status and Discount
        if status == "Regular":
            self.manager.output.status.text = "Regular"
            self.manager.output.discount.text = "None"
        else:
            self.manager.output.status.text = "Discounted"
            self.manager.output.discount.text = "20%"

        # Transit
        self.manager.output.transit.text = starting_place3+" - "+destination3

        # Total

        # Getting the distance of starting place and destination in km
        distance1 = int(starting_place_3.index(starting_place3))
        distance2 = int(starting_place_3.index(destination3))

        # Subtracting the distance of the two to get the final distance
        total_distance3 = abs(distance1 - distance2)

        self.manager.output.distance.text = str(total_distance3) + " KM"

        # Number of passenger
        number_of_passenger3 = int(passenger3)

        # Minimum Fare
        minimum_fare3 = int(minimum_fare3)

        # When the total distance is less than 4 then the tentative cost = 9 (Minimum Fare)
        if total_distance3 <= 4:
            tentative_cost = minimum_fare3 * number_of_passenger3
        # Else, the total distance is the result of the formula below.
        else:
            tentative_cost = (((total_distance3 - 4) * 1.50) + minimum_fare3) * number_of_passenger3

        # If status is student/ elderly/ disabled, discount is 20%
        if status == "Regular":
            fare_cost = tentative_cost
        else:
            discount_ = round((tentative_cost * 0.20), 2)
            fare_cost = tentative_cost - discount_

        self.manager.output.total.text = "₱ " + str('{:.2f}'.format(fare_cost))  # The fare cost

    def refresh3(self):
        self.ids.starting_place3.text = ''
        self.ids.destination3.text = ''
        self.ids.passenger3.text = '1'
        self.ids.minimum_fare3.text = '9'

    def invalid_input(self):
        close_button = MDFlatButton(
            text='CLOSE',
            text_color=[0, 0, 0, 1],
            on_release=self.close_dialog,
        )
        self.dialog = MDDialog(
            title='[color=#FF0000]Ooops![/color]',
            text='[color=#000000]There was an error processing your data. Kindly fill-up all the required information correctly to proceed to the next step. Thank you![/color]',
            size_hint=(0.9, 1),
            radius=[20, 7, 20, 7],
            buttons=[close_button],
        )
        self.dialog.open()

    # Close operation
    def close_dialog(self, obj):
        self.dialog.dismiss()


class OutputWindow(Screen):

    Builder.load_file('output_window.kv')

    def reset(self):
        self.manager.second.starting_place1.text = ''
        self.manager.second.destination1.text = ''
        self.manager.second.minimum_fare1.text = '9'
        self.manager.second.passenger1.text = '1'

        self.manager.second.starting_place2.text = ''
        self.manager.second.destination2.text = ''
        self.manager.second.minimum_fare2.text = '9'
        self.manager.second.passenger2.text = '1'

        self.manager.second.starting_place3.text = ''
        self.manager.second.destination3.text = ''
        self.manager.second.minimum_fare3.text = '9'
        self.manager.second.passenger3.text = '1'

        self.ids.status.text = ''
        self.ids.discount.text = ''
        self.ids.transit.text = ''
        self.ids.total.text = ''
        self.ids.distance.test = ''

        self.manager.current = "main"
        self.manager.transition.direction = "right"

        
class WindowManager(ScreenManager):
    pass


class paraApp(MDApp):

    def build(self):

        return WindowManager()


if __name__ == '__main__':
    paraApp().run()
