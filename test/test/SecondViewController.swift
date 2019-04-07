//
//  SecondViewController.swift
//  test
//
//  Created by Jaivignesh Venugopal on 4/6/19.
//  Copyright © 2019 Jaivignesh Venugopal. All rights reserved.
//

import UIKit
import CoreLocation


class SecondViewController: UIViewController, CLLocationManagerDelegate{
    
    @IBOutlet weak var idLabel: UILabel!
    var locationManager: CLLocationManager!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        locationManager = CLLocationManager()
        locationManager.requestAlwaysAuthorization()
        if CLLocationManager.locationServicesEnabled() {
            locationManager.delegate = self
            locationManager.desiredAccuracy = kCLLocationAccuracyNearestTenMeters
            locationManager.startUpdatingLocation()
        }
    }
    
    override func viewDidAppear(_ animated: Bool) {
        sleep(1)
        idLabel.text="ID: \(ID.value)"
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        guard let locValue: CLLocationCoordinate2D = manager.location?.coordinate else { return }
        print("locations = \(locValue.latitude) \(locValue.longitude)")
        let json: [String: Any] = [
            "client_id": ID.value,
            "longitude": locValue.longitude,
            "latitude": locValue.latitude,
            "unix_time": Int64(Date().timeIntervalSince1970*1000)
        ]
        
        let jsonData = try? JSONSerialization.data(withJSONObject: json)
        
        // create post request
        let url = URL(string: "https://33132f65.ngrok.io/save_location_and_time")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        
        // insert json data to the request
        request.httpBody = jsonData
        
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            guard let data = data, error == nil else {
                print(error?.localizedDescription ?? "No data")
                return
            }
            let responseJSON = try? JSONSerialization.jsonObject(with: data, options: [])
            if let responseJSON = responseJSON as? [String: Any] {
                print(responseJSON)
            }
        }
        
        task.resume()
    }
    
    
}
