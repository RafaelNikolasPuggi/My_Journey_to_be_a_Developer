import { View } from "./views.js";
export class MensagemView extends View {
    template(model) {
        return `
        <p class='alert alert-info'>${model}</p>
        `;
    }
}
