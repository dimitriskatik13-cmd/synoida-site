import Foundation
import Vision
import CoreImage
import AppKit
// usage: swift cutcrop.swift <in.jpg> <outdir> <tag> x y w h   (normalized crop, origin top-left)
let a = CommandLine.arguments
let inURL = URL(fileURLWithPath: a[1]); let outDir = URL(fileURLWithPath: a[2]); let tag = a[3]
let nx = Double(a[4])!, ny = Double(a[5])!, nw = Double(a[6])!, nh = Double(a[7])!
try? FileManager.default.createDirectory(at: outDir, withIntermediateDirectories: true)
guard let full = CIImage(contentsOf: inURL) else { print("cannot load"); exit(1) }
let W = full.extent.width, H = full.extent.height
// CIImage origin is bottom-left
let rect = CGRect(x: nx*W, y: (1-ny-nh)*H, width: nw*W, height: nh*H)
let crop = full.cropped(to: rect).transformed(by: CGAffineTransform(translationX: -rect.minX, y: -rect.minY))
let ctx = CIContext()
func save(_ img: CIImage, _ name: String) {
    guard let cg = ctx.createCGImage(img, from: img.extent) else { print("no cg"); return }
    let rep = NSBitmapImageRep(cgImage: cg)
    if let d = rep.representation(using: .png, properties: [:]) { try? d.write(to: outDir.appendingPathComponent(name)); print("wrote", name, Int(img.extent.width), Int(img.extent.height)) }
}
let handler = VNImageRequestHandler(ciImage: crop, options: [:])
let req = VNGenerateForegroundInstanceMaskRequest()
try! handler.perform([req])
guard let obs = req.results?.first else { print(tag, "no instances"); exit(2) }
let all = obs.allInstances
print(tag, "instances:", all.count, "crop px", Int(rect.minX), Int(H-rect.maxY), Int(rect.width), Int(rect.height))
if let m = try? obs.generateScaledMaskForImage(forInstances: all, from: handler) { save(CIImage(cvPixelBuffer: m), "\(tag)-mask.png") }
if let c = try? obs.generateMaskedImage(ofInstances: all, from: handler, croppedToInstancesExtent: false) { save(CIImage(cvPixelBuffer: c), "\(tag)-cut.png") }
for i in all.sorted() { if let m = try? obs.generateScaledMaskForImage(forInstances: IndexSet(integer: i), from: handler) { save(CIImage(cvPixelBuffer: m), "\(tag)-inst\(i)-mask.png") } }
