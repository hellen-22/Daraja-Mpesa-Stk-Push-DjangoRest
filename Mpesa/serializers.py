from rest_framework import serializers, response, status
from .validators import validate_possible_number

from .utils import MpesaGateWay

pay = MpesaGateWay()

class SendSTKPushSerializer(serializers.Serializer):
    phonenumber = serializers.CharField()
    amount = serializers.CharField()

    def validate_amount(self, attrs):
        amount = int(attrs)

        if amount <= 0:
            raise serializers.ValidationError(detail="Amount must be greater than 0")
        return amount

    def validate_phonenumber(self, attrs):
        phonenumber = attrs

        try:
            validate_possible_number(phonenumber, "KE")
            return phonenumber
        except:
            raise serializers.ValidationError(detail="Invalid Phone Number")
        

    def create(self, validated_data):
        phonenumber = validated_data['phonenumber']
        amount = validated_data['amount']

        if str(phonenumber)[0] == "+":
            phonenumber = phonenumber[1:]
        elif str(phonenumber)[0] == "0":
            phonenumber = "254" + phonenumber[1:]

        callback_url = 'https://lehky.co/'
        payment = pay.stk_push(phonenumber=phonenumber, amount=amount, callback_url=callback_url)

        res = payment.json()

        return res
        
                