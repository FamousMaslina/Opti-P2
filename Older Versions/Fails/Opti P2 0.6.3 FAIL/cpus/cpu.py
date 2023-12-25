import platform
import psutil

def get_processor_name():
  """Gets the name of the processor.

  Returns:
    The name of the processor as a string.
  """

  processor_name = platform.processor()
  return processor_name

def get_processor_frequency():
  """Gets the frequency of the processor.

  Returns:
    The frequency of the processor as an integer.
  """

  frequency = psutil.cpu_freq().current
  return frequency

processor_name = get_processor_name()
processor_frequency = get_processor_frequency()
cName = processor_name
cFreq = processor_frequency
cFreqS = str(cFreq)
cFreqUnit = "MHz"
asdawd2k3a403 = True
laptophardware = False
  #print("The name of the processor is: {}".format(processor_name))
  #print("The frequency of the processor is: {} {}".format(cFreqS, cFreqUnit))