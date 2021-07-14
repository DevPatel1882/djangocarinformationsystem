from django.db import models

# Create your models here.


class Feedback(models.Model):
    feedback = models.TextField()
    Short_Summery = models.CharField(max_length=400)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email
# contact model
class contact(models.Model):
    sno = models.AutoField
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    comment = models.TextField(max_length=500)

    def __str__(self):
          return self.name
# sell car form model
class Sell_Car_details(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_num = models.IntegerField()
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    car_company = models.CharField(max_length=100)
    car_year = models.CharField(max_length=100)
    car_model = models.CharField(max_length=200)
    kms_driven = models.CharField(max_length=200)
    fule_type = models.CharField(max_length=200,default="")
    car_ownership = models.CharField(max_length=300)
    Expected_price = models.CharField(max_length=200)
    car_img = models.ImageField(upload_to="car_data/sell_car_img")


    def __str__(self):
        return self.email





# maruti suzuki models
class maruti_arena(models.Model):
    car_id = models.AutoField(primary_key=True)
    main_img = models.ImageField(upload_to="car_data/images",default="")
    price_in_city = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100,default="")
    ex_showroom_price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=500,default="")
    specs_features_and_price = models.TextField(default="")
    first_img = models.ImageField(upload_to="car_data/images",default="")
    second_img = models.ImageField(upload_to="car_data/images", default="")
    third_img = models.ImageField(upload_to="car_data/images", default="")



    def __str__(self):
        return self.car_name

class maruti_nexa(models.Model):
    car_id = models.AutoField(primary_key=True)
    main_img = models.ImageField(upload_to="car_data/images",default="")
    price_in_city = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100,default="")
    ex_showroom_price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=500, default="")
    specs_features_and_price = models.TextField(default="")
    first_img = models.ImageField(upload_to="car_data/images", default="")
    second_img = models.ImageField(upload_to="car_data/images", default="")
    third_img = models.ImageField(upload_to="car_data/images", default="")

    #  Key Specifications  models
    ARAI_Mileage = models.CharField(max_length=400,default="")
    Fuel_Type = models.CharField(max_length=400, default="")
    Engine_Displacement = models.CharField(max_length=400, default="")
    Max_Power = models.CharField(max_length=400, default="")
    Max_Torque = models.CharField(max_length=400, default="")
    Seating_Capacity = models.CharField(max_length=400, default="")
    TransmissionType = models.CharField(max_length=400, default="")
    Boot_Space = models.CharField(max_length=400, default="")
    Fuel_Tank_Capacity = models.CharField(max_length=400, default="")
    Body_Type = models.CharField(max_length=400, default="")
    Service_Cost = models.CharField(max_length=400, default="")

    # Key Features of car  models
    Power_Windows_Front = models.CharField(max_length=300,default="")
    Air_Conditioner = models.CharField(max_length=300, default="")
    Passenger_Airbag = models.CharField(max_length=300, default="")
    Fog_Lights_Front = models.CharField(max_length=300, default="")
    Power_Steering = models.CharField(max_length=300, default="")
    Anti_Lock_Braking_System = models.CharField(max_length=300, default="")
    Driver_Airbag = models.CharField(max_length=300, default="")
    Automatic_Climate_Control = models.CharField(max_length=300, default="")
    Alloy_Wheels = models.CharField(max_length=300, default="")




    def __str__(self):
        return self.car_name



# tata car company model hear
class tata_moter(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_company = models.CharField(max_length=200,default="")
    main_img = models.ImageField(upload_to="car_data/images",default="")
    price_in_city = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100,default="")
    ex_showroom_price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=500, default="")
    specs_features_and_price = models.TextField(default="")
    first_img = models.ImageField(upload_to="car_data/images", default="")
    second_img = models.ImageField(upload_to="car_data/images", default="")
    third_img = models.ImageField(upload_to="car_data/images", default="")

    #  Key Specifications  models
    ARAI_Mileage = models.CharField(max_length=400,default="")
    Fuel_Type = models.CharField(max_length=400, default="")
    Engine_Displacement = models.CharField(max_length=400, default="")
    Max_Power = models.CharField(max_length=400, default="")
    Max_Torque = models.CharField(max_length=400, default="")
    Seating_Capacity = models.CharField(max_length=400, default="")
    TransmissionType = models.CharField(max_length=400, default="")
    Boot_Space = models.CharField(max_length=400, default="")
    Fuel_Tank_Capacity = models.CharField(max_length=400, default="")
    Body_Type = models.CharField(max_length=400, default="")
    Service_Cost = models.CharField(max_length=400, default="")

    # Key Features of car  models
    Power_Windows_Front = models.CharField(max_length=300,default="")
    Air_Conditioner = models.CharField(max_length=300, default="")
    Passenger_Airbag = models.CharField(max_length=300, default="")
    Fog_Lights_Front = models.CharField(max_length=300, default="")
    Power_Steering = models.CharField(max_length=300, default="")
    Anti_Lock_Braking_System = models.CharField(max_length=300, default="")
    Driver_Airbag = models.CharField(max_length=300, default="")
    Automatic_Climate_Control = models.CharField(max_length=300, default="")
    Alloy_Wheels = models.CharField(max_length=300, default="")




    def __str__(self):
        return self.car_name


# jaguar car company model hear
class jaguar_moter(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_company = models.CharField(max_length=200,default="")
    main_img = models.ImageField(upload_to="car_data/images",default="")
    price_in_city = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100,default="")
    ex_showroom_price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=500, default="")
    specs_features_and_price = models.TextField(default="")
    first_img = models.ImageField(upload_to="car_data/images", default="")
    second_img = models.ImageField(upload_to="car_data/images", default="")
    third_img = models.ImageField(upload_to="car_data/images", default="")

    #  Key Specifications  models
    ARAI_Mileage = models.CharField(max_length=400,default="")
    Fuel_Type = models.CharField(max_length=400, default="")
    Engine_Displacement = models.CharField(max_length=400, default="")
    Max_Power = models.CharField(max_length=400, default="")
    Max_Torque = models.CharField(max_length=400, default="")
    Seating_Capacity = models.CharField(max_length=400, default="")
    TransmissionType = models.CharField(max_length=400, default="")
    Boot_Space = models.CharField(max_length=400, default="")
    Fuel_Tank_Capacity = models.CharField(max_length=400, default="")
    Body_Type = models.CharField(max_length=400, default="")
    Service_Cost = models.CharField(max_length=400, default="")

    # Key Features of car  models
    Power_Windows_Front = models.CharField(max_length=300,default="")
    Air_Conditioner = models.CharField(max_length=300, default="")
    Passenger_Airbag = models.CharField(max_length=300, default="")
    Fog_Lights_Front = models.CharField(max_length=300, default="")
    Power_Steering = models.CharField(max_length=300, default="")
    Anti_Lock_Braking_System = models.CharField(max_length=300, default="")
    Driver_Airbag = models.CharField(max_length=300, default="")
    Automatic_Climate_Control = models.CharField(max_length=300, default="")
    Alloy_Wheels = models.CharField(max_length=300, default="")




    def __str__(self):
        return self.car_name

# mahindra car company model hear
class mahindra_moter(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_company = models.CharField(max_length=200,default="")
    main_img = models.ImageField(upload_to="car_data/images",default="")
    price_in_city = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100,default="")
    ex_showroom_price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=500, default="")
    specs_features_and_price = models.TextField(default="")
    first_img = models.ImageField(upload_to="car_data/images", default="")
    second_img = models.ImageField(upload_to="car_data/images", default="")
    third_img = models.ImageField(upload_to="car_data/images", default="")

    #  Key Specifications  models
    ARAI_Mileage = models.CharField(max_length=400,default="")
    Fuel_Type = models.CharField(max_length=400, default="")
    Engine_Displacement = models.CharField(max_length=400, default="")
    Max_Power = models.CharField(max_length=400, default="")
    Max_Torque = models.CharField(max_length=400, default="")
    Seating_Capacity = models.CharField(max_length=400, default="")
    TransmissionType = models.CharField(max_length=400, default="")
    Boot_Space = models.CharField(max_length=400, default="")
    Fuel_Tank_Capacity = models.CharField(max_length=400, default="")
    Body_Type = models.CharField(max_length=400, default="")
    Service_Cost = models.CharField(max_length=400, default="")

    # Key Features of car  models
    Power_Windows_Front = models.CharField(max_length=300,default="")
    Air_Conditioner = models.CharField(max_length=300, default="")
    Passenger_Airbag = models.CharField(max_length=300, default="")
    Fog_Lights_Front = models.CharField(max_length=300, default="")
    Power_Steering = models.CharField(max_length=300, default="")
    Anti_Lock_Braking_System = models.CharField(max_length=300, default="")
    Driver_Airbag = models.CharField(max_length=300, default="")
    Automatic_Climate_Control = models.CharField(max_length=300, default="")
    Alloy_Wheels = models.CharField(max_length=300, default="")




    def __str__(self):
        return self.car_name

class hundai_moter(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_company = models.CharField(max_length=200,default="")
    main_img = models.ImageField(upload_to="car_data/images",default="")
    price_in_city = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100,default="")
    ex_showroom_price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=500, default="")
    specs_features_and_price = models.TextField(default="")
    first_img = models.ImageField(upload_to="car_data/images", default="")
    second_img = models.ImageField(upload_to="car_data/images", default="")
    third_img = models.ImageField(upload_to="car_data/images", default="")

    #  Key Specifications  models
    ARAI_Mileage = models.CharField(max_length=400,default="")
    Fuel_Type = models.CharField(max_length=400, default="")
    Engine_Displacement = models.CharField(max_length=400, default="")
    Max_Power = models.CharField(max_length=400, default="")
    Max_Torque = models.CharField(max_length=400, default="")
    Seating_Capacity = models.CharField(max_length=400, default="")
    TransmissionType = models.CharField(max_length=400, default="")
    Boot_Space = models.CharField(max_length=400, default="")
    Fuel_Tank_Capacity = models.CharField(max_length=400, default="")
    Body_Type = models.CharField(max_length=400, default="")
    Service_Cost = models.CharField(max_length=400, default="")

    # Key Features of car  models
    Power_Windows_Front = models.CharField(max_length=300,default="")
    Air_Conditioner = models.CharField(max_length=300, default="")
    Passenger_Airbag = models.CharField(max_length=300, default="")
    Fog_Lights_Front = models.CharField(max_length=300, default="")
    Power_Steering = models.CharField(max_length=300, default="")
    Anti_Lock_Braking_System = models.CharField(max_length=300, default="")
    Driver_Airbag = models.CharField(max_length=300, default="")
    Automatic_Climate_Control = models.CharField(max_length=300, default="")
    Alloy_Wheels = models.CharField(max_length=300, default="")




    def __str__(self):
        return self.car_name

class honda_moter(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_company = models.CharField(max_length=200,default="")
    main_img = models.ImageField(upload_to="car_data/images",default="")
    price_in_city = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100,default="")
    ex_showroom_price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=500, default="")
    specs_features_and_price = models.TextField(default="")
    first_img = models.ImageField(upload_to="car_data/images", default="")
    second_img = models.ImageField(upload_to="car_data/images", default="")
    third_img = models.ImageField(upload_to="car_data/images", default="")

    #  Key Specifications  models
    ARAI_Mileage = models.CharField(max_length=400,default="")
    Fuel_Type = models.CharField(max_length=400, default="")
    Engine_Displacement = models.CharField(max_length=400, default="")
    Max_Power = models.CharField(max_length=400, default="")
    Max_Torque = models.CharField(max_length=400, default="")
    Seating_Capacity = models.CharField(max_length=400, default="")
    TransmissionType = models.CharField(max_length=400, default="")
    Boot_Space = models.CharField(max_length=400, default="")
    Fuel_Tank_Capacity = models.CharField(max_length=400, default="")
    Body_Type = models.CharField(max_length=400, default="")
    Service_Cost = models.CharField(max_length=400, default="")

    # Key Features of car  models
    Power_Windows_Front = models.CharField(max_length=300,default="")
    Air_Conditioner = models.CharField(max_length=300, default="")
    Passenger_Airbag = models.CharField(max_length=300, default="")
    Fog_Lights_Front = models.CharField(max_length=300, default="")
    Power_Steering = models.CharField(max_length=300, default="")
    Anti_Lock_Braking_System = models.CharField(max_length=300, default="")
    Driver_Airbag = models.CharField(max_length=300, default="")
    Automatic_Climate_Control = models.CharField(max_length=300, default="")
    Alloy_Wheels = models.CharField(max_length=300, default="")




    def __str__(self):
        return self.car_name

class ford_moter(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_company = models.CharField(max_length=200,default="")
    main_img = models.ImageField(upload_to="car_data/images",default="")
    price_in_city = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100,default="")
    ex_showroom_price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=500, default="")
    specs_features_and_price = models.TextField(default="")
    first_img = models.ImageField(upload_to="car_data/images", default="")
    second_img = models.ImageField(upload_to="car_data/images", default="")
    third_img = models.ImageField(upload_to="car_data/images", default="")

    #  Key Specifications  models
    ARAI_Mileage = models.CharField(max_length=400,default="")
    Fuel_Type = models.CharField(max_length=400, default="")
    Engine_Displacement = models.CharField(max_length=400, default="")
    Max_Power = models.CharField(max_length=400, default="")
    Max_Torque = models.CharField(max_length=400, default="")
    Seating_Capacity = models.CharField(max_length=400, default="")
    TransmissionType = models.CharField(max_length=400, default="")
    Boot_Space = models.CharField(max_length=400, default="")
    Fuel_Tank_Capacity = models.CharField(max_length=400, default="")
    Body_Type = models.CharField(max_length=400, default="")
    Service_Cost = models.CharField(max_length=400, default="")

    # Key Features of car  models
    Power_Windows_Front = models.CharField(max_length=300,default="")
    Air_Conditioner = models.CharField(max_length=300, default="")
    Passenger_Airbag = models.CharField(max_length=300, default="")
    Fog_Lights_Front = models.CharField(max_length=300, default="")
    Power_Steering = models.CharField(max_length=300, default="")
    Anti_Lock_Braking_System = models.CharField(max_length=300, default="")
    Driver_Airbag = models.CharField(max_length=300, default="")
    Automatic_Climate_Control = models.CharField(max_length=300, default="")
    Alloy_Wheels = models.CharField(max_length=300, default="")




    def __str__(self):
        return self.car_name


class renult_moter(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_company = models.CharField(max_length=200,default="")
    main_img = models.ImageField(upload_to="car_data/images",default="")
    price_in_city = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100,default="")
    ex_showroom_price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=500, default="")
    specs_features_and_price = models.TextField(default="")
    first_img = models.ImageField(upload_to="car_data/images", default="")
    second_img = models.ImageField(upload_to="car_data/images", default="")
    third_img = models.ImageField(upload_to="car_data/images", default="")

    #  Key Specifications  models
    ARAI_Mileage = models.CharField(max_length=400,default="")
    Fuel_Type = models.CharField(max_length=400, default="")
    Engine_Displacement = models.CharField(max_length=400, default="")
    Max_Power = models.CharField(max_length=400, default="")
    Max_Torque = models.CharField(max_length=400, default="")
    Seating_Capacity = models.CharField(max_length=400, default="")
    TransmissionType = models.CharField(max_length=400, default="")
    Boot_Space = models.CharField(max_length=400, default="")
    Fuel_Tank_Capacity = models.CharField(max_length=400, default="")
    Body_Type = models.CharField(max_length=400, default="")
    Service_Cost = models.CharField(max_length=400, default="")

    # Key Features of car  models
    Power_Windows_Front = models.CharField(max_length=300,default="")
    Air_Conditioner = models.CharField(max_length=300, default="")
    Passenger_Airbag = models.CharField(max_length=300, default="")
    Fog_Lights_Front = models.CharField(max_length=300, default="")
    Power_Steering = models.CharField(max_length=300, default="")
    Anti_Lock_Braking_System = models.CharField(max_length=300, default="")
    Driver_Airbag = models.CharField(max_length=300, default="")
    Automatic_Climate_Control = models.CharField(max_length=300, default="")
    Alloy_Wheels = models.CharField(max_length=300, default="")




    def __str__(self):
        return self.car_name


class nissan_moter(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_company = models.CharField(max_length=200,default="")
    main_img = models.ImageField(upload_to="car_data/images",default="")
    price_in_city = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=200)
    car_name = models.CharField(max_length=100,default="")
    ex_showroom_price = models.CharField(max_length=200)
    reviews = models.CharField(max_length=500, default="")
    specs_features_and_price = models.TextField(default="")
    first_img = models.ImageField(upload_to="car_data/images", default="")
    second_img = models.ImageField(upload_to="car_data/images", default="")
    third_img = models.ImageField(upload_to="car_data/images", default="")

    #  Key Specifications  models
    ARAI_Mileage = models.CharField(max_length=400,default="")
    Fuel_Type = models.CharField(max_length=400, default="")
    Engine_Displacement = models.CharField(max_length=400, default="")
    Max_Power = models.CharField(max_length=400, default="")
    Max_Torque = models.CharField(max_length=400, default="")
    Seating_Capacity = models.CharField(max_length=400, default="")
    TransmissionType = models.CharField(max_length=400, default="")
    Boot_Space = models.CharField(max_length=400, default="")
    Fuel_Tank_Capacity = models.CharField(max_length=400, default="")
    Body_Type = models.CharField(max_length=400, default="")
    Service_Cost = models.CharField(max_length=400, default="")

    # Key Features of car  models
    Power_Windows_Front = models.CharField(max_length=300,default="")
    Air_Conditioner = models.CharField(max_length=300, default="")
    Passenger_Airbag = models.CharField(max_length=300, default="")
    Fog_Lights_Front = models.CharField(max_length=300, default="")
    Power_Steering = models.CharField(max_length=300, default="")
    Anti_Lock_Braking_System = models.CharField(max_length=300, default="")
    Driver_Airbag = models.CharField(max_length=300, default="")
    Automatic_Climate_Control = models.CharField(max_length=300, default="")
    Alloy_Wheels = models.CharField(max_length=300, default="")




    def __str__(self):
        return self.car_name