//
//  ViewController.swift
//  test
//
//  Created by Jaivignesh Venugopal on 4/6/19.
//  Copyright © 2019 Jaivignesh Venugopal. All rights reserved.
//

import UIKit

struct ID {
    static var value = "-1"
}

class TestViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    func setID(id: String) {
        // set ID
        ID.value = id
        print(ID.value)
        
    }
    
    @IBAction func pressSomeButton(_ sender: UIButton) {
        let idURL = URL(string: "https://33132f65.ngrok.io/get_id")!
        let task = URLSession.shared.dataTask(with: idURL){(data, response, error) in
            if (error == nil) {
                let loadedID = String(bytes: data!, encoding: .utf8)!
                self.setID(id: loadedID)
            }
        }
        task.resume()

    }
}
