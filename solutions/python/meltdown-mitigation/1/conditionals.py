"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature<800 and neutrons_emitted>500 and temperature*neutrons_emitted<500000
            

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage = (generated_power/theoretical_max_power)*100
    if percentage>=80:
        return 'green'
    elif percentage>=60:
        return 'orange'
    elif percentage>=30:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    threshold90= 0.90*threshold
    threshold10= 1.1*threshold

    if (temperature * neutrons_produced_per_second)< threshold90:
        return 'LOW'
    elif (temperature * neutrons_produced_per_second)< threshold10:
        return 'NORMAL'
    else: 
        return 'DANGER'