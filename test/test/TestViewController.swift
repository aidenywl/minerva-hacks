//
//  ViewController.swift
//  test
//
//  Created by Jaivignesh Venugopal on 4/6/19.
//  Copyright © 2019 Jaivignesh Venugopal. All rights reserved.
//

import UIKit

class TestViewController: UIViewController {
    @IBOutlet weak var myLabel: UILabel!
    
    var count = 0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
    
    @IBAction func pressSomeButton(_ sender: UIButton) {
        print(sender.titleLabel!.text)
        
        count += 1
        myLabel.text = "count \(count)"
    }

}
