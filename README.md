Upon clicking my submit button I was sent to
{
        fortune_results?
        name (key) = Dillard (value)
        &
        concentration (key) = BEW (value)
        &
        birthday (key)= (value)
        &
        crafts (key) = logs (value)

}

My values correspond to the choices the user made, or at least the name I specified in the html element of the corresponding form.


The data in the weather response is in JSON object format... we can discern a small variety of data from the object. Some fields contain data we don't know how to interpret.

In order to find the temperature in the specified city we would call the key "temp"
