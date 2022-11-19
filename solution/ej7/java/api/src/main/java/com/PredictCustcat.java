package com;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import org.json.JSONException;
import org.json.JSONObject;

@Controller
public class PredictCustcat {
	
	// Method to validate JSON file
	private Boolean validateJSON(JSONObject json) {
		try {
			json.getString("region");
			json.getString("tenure");
			json.getString("age");
			json.getString("marital");
			json.getString("address");
			json.getString("income");
			json.getString("ed");
			json.getString("employ");
			json.getString("retired");
			json.getString("gender");
			json.getString("reside");
			if (!json.getString("marital").equals("single") && !json.getString("marital").equals("married")) {
				return false;
			}
			return true;
		} catch (JSONException e) {
			return false;
		}
	}

	@GetMapping("/api/predict/custcat")
	public ResponseEntity<String> predict_custcat(@RequestBody String json) throws JSONException {
		
		// Attempt to get parse JSON object
		JSONObject js = null;
		try {
			js = new JSONObject(json);
		} catch (JSONException e) {
			e.printStackTrace();
		}
		
		// Validate JSON Object
		if (!validateJSON(js)) {
			return new ResponseEntity<String>("Datos ingresados incorrectamente.", HttpStatus.BAD_REQUEST);
		}
		
		// Generate requested values as strings
		String req_region = ""; String req_tenure = ""; String req_age = ""; String req_marital = ""; String req_address = ""; String req_income = "";
		String req_ed = ""; String req_employ = ""; String req_retired = ""; String req_gender = ""; String req_reside = "";
		
		// Load requested values
		try {
			req_region = js.getString("region");
			req_tenure = js.getString("tenure");
			req_age = js.getString("age");
			req_marital = js.getString("marital");
			if (req_marital.equals("single")) {
				req_marital = "0";
			} else {
				req_marital = "1";
			}
			req_address = js.getString("address");
			req_income = js.getString("income");
			req_ed = js.getString("ed");
			req_employ = js.getString("employ");
			req_retired = js.getString("retired");
			if (req_retired.equals("true")) {
				req_retired = "1.000";
			} else {
				req_retired = "0.000";
			}
			req_gender = js.getString("gender");
			if (req_gender.equals("true")) {
				req_gender = "1";
			} else {
				req_gender = "0";
			}
			req_reside = js.getString("reside");
		} catch (JSONException e1) {
			e1.printStackTrace();
		}
		
		// Scan for CSV file
		Scanner sc = null;
		try {
			sc = new Scanner(new File("C:/teleCust1000t.csv"));
			sc.useDelimiter("[,\n]");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		// Search for request
		
		// Determine if we found the record
		boolean found = false;
		
		// Variables for loading each field
		String region = ""; String tenure = ""; String age = ""; String marital = ""; String address = ""; String income = "";
		String ed = ""; String employ = ""; String retired = ""; String gender = ""; String reside = "";
		
		// Loop for finding record
		while (sc.hasNext() && !found) {
			
			// Load variables
			region = sc.next();
			tenure = sc.next();
			age = sc.next();
			marital = sc.next();
			address = sc.next();
			income = sc.next();
			income = income.replace(".", "");
			ed = sc.next();
			employ = sc.next();
			retired = sc.next();
			gender = sc.next();
			reside = sc.next();
			
			// Check if record matches request
			if (req_region.equals(region) && req_tenure.equals(tenure) && req_age.equals(age) && req_marital.equals(marital) &&
					req_address.equals(address) && req_income.equals(income) && req_ed.equals(ed) && req_employ.equals(employ) &&
					req_retired.equals(retired) && req_gender.equals(gender) && req_reside.equals(reside)) {
				found = true;
				break;
			}
			
			// Skip last column
			sc.next();
			
		}
		
		// Check if request was found
		if (found) {
			return new ResponseEntity<String>(sc.next(), HttpStatus.OK);
		} else {
			return new ResponseEntity<String>("Registro no encontrado", HttpStatus.INTERNAL_SERVER_ERROR);
		}
		
	}
	
}
