//
//  CircleImage.swift
//  Landmark
//
//  Created by Taylor Johnson on 10/19/23.
//

import SwiftUI


struct CircleImage: View {
    var image: Image

    var body: some View {
        image
            .clipShape(Circle())
            .overlay {
                Circle().stroke(.white, lineWidth: 4)
            }
            .shadow(radius: 7)
    }
}

#Preview {
    CircleImage(image: Image("turtlerock"))
}
