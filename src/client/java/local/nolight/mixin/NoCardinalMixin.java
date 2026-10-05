package local.nolight.mixin;

import net.minecraft.core.Direction;
import net.minecraft.world.level.CardinalLighting;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

@Mixin(CardinalLighting.class)
public class NoCardinalMixin {
	// Все грани получают одинаковую яркость (1.0)
	@Inject(method = "byFace", at = @At("HEAD"), cancellable = true)
	private void nolight$flat(Direction direction, CallbackInfoReturnable<Float> cir) {
		cir.setReturnValue(1.0F);
	}
}
