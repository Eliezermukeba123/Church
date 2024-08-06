import requests

endpoint = "https://app.chmeetings.com/F17B18D8A37CEFD0/Core/Dashboard"
response = requests.get(endpoint)
print(response.text)


<div class="flex flex-col md:flex md:flex-row md:space-x-2">

            <div class="md:flex md:w-1/2 w-full flex flex-col">
               <label  class="block text-sm font-bold text-gray-700">{{ form.nombre_offrandes.label }}</label>
            {{ form.nombre_offrandes|add_class:"mt-1 focus:border-bright focus:outline-none block w-full sm:text-sm border-gray-300 rounded-md" }}

            </div>
            <div class="md:flex md:w-1/2 w-full flex flex-col">
                 <label  class="block text-sm font-bold text-gray-700">{{ form.nombre_construction.label }}</label>
            {{ form.nombre_construction|add_class:"mt-1 focus:border-bright focus:outline-none block w-full sm:text-sm border-gray-300 rounded-md" }}

            </div>

        </div>