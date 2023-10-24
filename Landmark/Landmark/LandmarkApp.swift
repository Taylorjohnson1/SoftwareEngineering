//
//  LandmarkApp.swift
//  Landmark
//
//  Created by Taylor Johnson on 10/19/23.
//

import SwiftUI

@main
struct LandmarksApp: App {
    @State private var modelData = ModelData()


    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(modelData)
        }
    }
}
