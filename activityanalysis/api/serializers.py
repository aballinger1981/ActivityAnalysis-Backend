from rest_framework import serializers
from api.models import RunTotal, RideTotal, SwimTotal, Athlete, Bike, Shoe, Gear, Activity, Lap, SplitMetric, SplitStandard

class RunTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunTotal
        fields = ('id', 'count', 'distance', 'moving_time', 'elapsed_time', 'elevation_gain')

class RideTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideTotal
        fields = ('id', 'count', 'distance', 'moving_time', 'elapsed_time', 'elevation_gain')

class SwimTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimTotal
        fields = ('id', 'count', 'distance', 'moving_time', 'elapsed_time', 'elevation_gain')

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ('first_name', 'last_name', 'profile_medium', 'profile', 'city', 'state', 'country', 'sex', 'email', 'weight', 'run_total', 'ride_total', 'swim_total')

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ('athlete_id', 'name', 'distance', 'primary')

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = ('athlete_id', 'name', 'distance', 'primary')

class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = ('primary_gear', 'gear_name', 'gear_distance')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('athlete_id', 'name', 'description', 'distance', 'moving_time', 'elapsed_time', 'total_elevation_gain', 'elev_high', 'elev_low', 'activity_type', 'start_date', 'start_date_local', 'timezone', 'start_latlng', 'end_latlng', 'map_polyline', 'trainer', 'commute', 'manual', 'gear', 'average_speed', 'max_speed', 'calories', 'average_cadence')

class LapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lap
        fields = ('activity_id', 'athlete_id', 'average_cadence', 'average_speed', 'distance', 'elapsed_time', 'end_index', 'lap_index', 'max_speed', 'moving_time', 'name', 'pace_zone', 'split', 'start_date', 'start_date_local', 'start_index', 'total_elevation_gain')

class SplitMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitMetric
        fields = ('activity_id', 'average_speed', 'distance', 'elapsed_time', 'elevation_difference', 'moving_time', 'pace_zone', 'split')

class SplitStandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitStandard
        fields = ('activity_id', 'average_speed', 'distance', 'elapsed_time', 'elevation_difference', 'moving_time', 'pace_zone', 'split')
