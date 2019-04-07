//
//  SecondViewController.swift
//  test
//
//  Created by Jaivignesh Venugopal on 4/6/19.
//  Copyright © 2019 Jaivignesh Venugopal. All rights reserved.
//

import UIKit

class SecondViewController: UIViewController {
    
    var timer: Timer!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        locationTrackerWithTimer()
    }
    
    func locationTrackerWithTimer() {
        // Scheduling timer to Call the function "updateCounting" with the interval of 1 seconds
        timer = Timer.scheduledTimer(timeInterval: 5, target: self, selector: #selector(sendLocation), userInfo: nil, repeats: true)
        
    }
    
    @objc func sendLocation() {
        print(Int64(Date().timeIntervalSince1970*1000))
    }
    
    
}
