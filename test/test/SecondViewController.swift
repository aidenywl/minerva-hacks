//
//  SecondViewController.swift
//  test
//
//  Created by Jaivignesh Venugopal on 4/6/19.
//  Copyright © 2019 Jaivignesh Venugopal. All rights reserved.
//

import Foundation

import UIKit

class SecondViewController: UIViewController {
    @IBOutlet weak var whateverLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        whateverLabel.alpha = 0.5
    }
    
    
}
