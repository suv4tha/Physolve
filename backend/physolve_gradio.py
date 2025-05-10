import gradio as gr
import math

# Define formulas and their required inputs
formulas = {
    "Average Speed (S = d/t)": (["d", "t"], lambda d, t: d / t),
    "Acceleration (a = (v - u)/t)": (["v", "u", "t"], lambda v, u, t: (v - u) / t),
    "Density (ρ = m/V)": (["m", "V"], lambda m, V: m / V),
    "Power (P = W/t)": (["W", "t"], lambda W, t: W / t),
    "Newton's Second Law (F = ma)": (["m", "a"], lambda m, a: m * a),
    "Weight (W = mg)": (["m", "g"], lambda m, g: m * g),
    "Pressure (P = F/A)": (["F", "A"], lambda F, A: F / A),
    "Ohm's Law (V = IR)": (["I", "R"], lambda I, R: I * R),
    "Kinetic Energy (E = ½mv²)": (["m", "v"], lambda m, v: 0.5 * m * v**2),
    "Pendulum Time (T = 2π√L/g)": (["L", "g"], lambda L, g: 2 * math.pi * math.sqrt(L / g)),
    # You can add more formulas here...
}

def calculate(formula_name, *args):
    inputs, formula_fn = formulas[formula_name]
    try:
        values = list(map(float, args[:len(inputs)]))
        result = formula_fn(*values)
        return f"✅ Result: {result:.4f}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def update_inputs(formula_name):
    fields = formulas[formula_name][0]
    updates = []

    for i in range(len(input_components)):
        if i < len(fields):
            updates.append(gr.update(visible=True, label=fields[i]))
        else:
            updates.append(gr.update(visible=False))
    return updates

with gr.Blocks(theme=gr.themes.Soft(primary_hue="violet")) as app:
    gr.Markdown("## 🎓 Physolve - Smart Physics Calculator")
    gr.Markdown("Select a formula and enter the required values below to calculate the result.")

    with gr.Row():
        selected_formula = gr.Dropdown(
            choices=list(formulas.keys()),
            label="🧪 Choose a Formula",
            value=None,
            interactive=True
        )

    with gr.Row():
        input_components = [gr.Number(visible=False, label=f"Input {i+1}") for i in range(5)]

    with gr.Row():
        calculate_btn = gr.Button("🚀 Calculate", variant="primary")
        output = gr.Textbox(label="📘 Result", lines=1)

    # Events
    selected_formula.change(fn=update_inputs, inputs=[selected_formula], outputs=input_components)
    calculate_btn.click(fn=calculate, inputs=[selected_formula] + input_components, outputs=[output])

app.launch()
