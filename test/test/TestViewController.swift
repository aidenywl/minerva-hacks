//
//  ViewController.swift
//  test
//
//  Created by Jaivignesh Venugopal on 4/6/19.
//  Copyright © 2019 Jaivignesh Venugopal. All rights reserved.
//

import UIKit
var ID: String = "-1"

class TestViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    func setID(id: String) {
        // set ID
        ID = id
        print(ID)
        
    }
    
    @IBAction func pressSomeButton(_ sender: UIButton) {
        let idURL = URL(string: "https://53d48747.ngrok.io/get_id")!
        let task = URLSession.shared.dataTask(with: idURL){(data, response, error) in
            if (error == nil) {
                let loadedID = String(bytes: data!, encoding: .utf8)!
                self.setID(id: loadedID)
            }
        }
        task.resume()

    }
}
