payload = {
	"request":
	{
		"passengers":
		{
			"adultCount":1,
			"kind":"qpxexpress#passengerCounts"
		},
		"saleCountry":"IN",
		"maxPrice":"INR5000",
		"solutions":500,
		"slice":
		[
			{
				"origin":"DEL",
				"destination":"BOM",
				"date":"2016-05-26",
				"permittedDepartureTime":
				{
					"earliestTime":"14:30",
					"latestTime":"15:30",
					"kind":"qpxexpress#timeOfDayRange",
				}
			}
		]
	}
}