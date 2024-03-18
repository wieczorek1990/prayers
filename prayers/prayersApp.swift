import SwiftUI
import MarkdownView

@main
struct prayersApp: App {
    var body: some Scene {
        WindowGroup {
            ScrollView {
                MarkdownUI(body: markdown)
            }
        }
    }

    private var markdown: String {
        let path = Bundle.main.path(forResource: "Modlitwy", ofType: "md")!
        let url = URL(fileURLWithPath: path)
        return try! String(contentsOf: url, encoding: String.Encoding.utf8)
    }
}
